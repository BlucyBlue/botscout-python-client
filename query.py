import re
import requests
from email.utils import parseaddr

from validate_email import validate_email

from conf import BASE_URL, KEY, VALID_Q_PARAMS

def validate_qparams(params):

	ip_pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

	formatted_params = {}

	for key in params.keys():
		if key not in VALID_Q_PARAMS:
			print(f"Removed invalid filter {key}.")
			break

		if key == "mail" and not validate_email(params[key]):
			print(f"Removed invalid email address {params[key]}.")

		elif key == "ip" and not re.match(ip_pattern, params[key]):
			print(f"Removed invalid IP addred {params[key]}")

		else:
			formatted_params[key] = params[key]

	assert len(formatted_params.keys()) > 0, "Could not find any valid query parameters."

	return formatted_params


def make_query(query_params, multiple=True):

	if KEY and "key" not in query_params.keys():
		query_params["key"] = KEY

	url = BASE_URL + "multi" if multiple else BASE_URL

	for k, v in query_params.items():
		url += f"&{k}={v}"

	response = requests.get(url)

	return response.content