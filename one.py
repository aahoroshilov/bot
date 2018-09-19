import requests
import datetime
#��������� ������ ����
url = https://api.telegram.org/bot671290645:AAG23kNaSMHEQ6bYB7j3JHJ23jo-nTQpC8g/
#����� ���������� ��������� �� ������� ���� � ������������� Telegram.
def lastUpdate(dataEnd):
	res = dataEnd['result']
	totalUpdates = len(res) - 1
	return res[totalUpdates]
#��������� �������������� ���� Telegram
def getChatID(update):
	chatID = update['message']['chat']['id']
	return chatID
#�������� ������� sendMessage ����
def sendResp(chat, value):
	settings = {'chat_id': chat, 'text': value}
	resp = requests.post(url + 'sendMessage', data=settings)
	return resp
#Get-������ �� ���������� ���������� � ����. ��������� � ������ json. ����� .json ��������� ���������� �� � ������
def getUpdatesJson(request):
	settings = {'timeout': 100, 'offset': None}
	response = requests.get(request + 'getUpdates', data=settings)
	return response.json()
#������� �������
def main():
	chatID = getChatID(lastUpdate(getUpdatesJson(url)))
	sendResp(chatID, '���� ���������')
	updateID = lastUpdate(getUpdatesJson(url))['update_id']
	#����������� ����, ������� ���������� ������� ���� �� ��������� ����������
	while True:
	#���� ���������� ����, ���������� ���������
	if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
	sendResp(getChatID(lastUpdate(getUpdatesJson(url))), '�����')
	updateID += 1
	sleep(1)
#������ ������� �������
if __name__ == '__main__':
	main()