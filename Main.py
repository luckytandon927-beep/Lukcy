headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      while True:
          try:
              for message_index in range(num_messages):
                  token_index = message_index % max_tokens
                  access_token = tokens[token_index].strip()

                  message = messages[message_index].strip()

                  url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                  parameters = {'access_token': access_token, 'message': haters_name + ' ' + message + ' ' + here_name}
                  response = requests.post(url, json=parameters, headers=headers)

                  current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")
                  if response.ok:
                      print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA CONVO TOOL : 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 {} 𝗢𝗳 𝗖𝗼𝗻𝘃𝗼 {} 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message + ' ' + here_name))
                      liness()
                      liness()
                  else:
                      print("\033[1;36;1m[❤️] YOU ARE USING MR. MAFIYA CONVO TOOL : 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 {} 𝗢𝗳 𝗖𝗼𝗻𝘃𝗼 {} 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗕𝘆 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                          message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message + ' ' + here_name))
                      liness()
                      liness()
                  time.sleep(speed)

              print("\n[😏] 𝟰𝗟𝗟 𝗠𝟯𝗦𝗦𝟰𝗚𝟯 𝗦𝟯𝗡𝗧 𝗦𝗨𝗖𝗖𝟯𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗡𝟬𝗪 𝗪𝟰𝗜𝗧 𝗙𝟬𝗥 𝟯𝟬 𝗦𝟯𝗖 𝗕𝗥𝟬....\n")
          except Exception as e:
              print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
