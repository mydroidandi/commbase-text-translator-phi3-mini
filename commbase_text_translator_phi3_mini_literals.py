#!/usr/bin/env python
################################################################################
#                  commbase_text_translator_phi3_mini_literals                 #
#                                                                              #
# A simple generative AI assistant using the Phi3 Small Language Model (SLM).  #
#                                                                              #
# Change History                                                               #
# 07/11/2024  Esteban Herrera Original code.                                   #
#                           Add new history entries as needed.                 #
#                                                                              #
#                                                                              #
################################################################################
################################################################################
################################################################################
#                                                                              #
#  Copyright (c) 2022-present Esteban Herrera C.                               #
#  stv.herrera@gmail.com                                                       #
#                                                                              #
#  This program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program; if not, write to the Free Software                 #
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   #

# commbase_text_translator_phi3_mini_literals.py
# TODO:
# Usage example:
# python commbase_text_translator_phi3_mini_literals.py """Your text containing "quotes" and 'single quotes'.""" english spanish

# Imports
import sys
import ollama


def prompt_user():
    # Check if the script received the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py \"Text to translate\" from_language to_language")
        sys.exit(1)

    # Get the text to translate and languages from command line arguments
    text_to_translate = sys.argv[1]
    from_language = sys.argv[2]
    to_language = sys.argv[3]

    return text_to_translate, from_language, to_language


def generate_response(text_to_translate, from_language, to_language):
    # Generate the response using the provided text and languages
    order = f"Translate this from {from_language} to {to_language}: "
    response = ollama.generate(model='commbase-phi3-mini', prompt=order + text_to_translate)

    # Extract the text response
    return response['response']


def main():
    # Prompt the user for input
    text_to_translate, from_language, to_language = prompt_user()

    # Generate the response based on the text and languages
    text_response = generate_response(text_to_translate, from_language, to_language)

    # Print the response to the terminal
    print(text_response)


if __name__ == "__main__":
    main()
