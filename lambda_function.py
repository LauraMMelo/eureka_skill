import logging
import ask_sdk_core.utils as ask_utils
import os
import requests
import calendar
from datetime import datetime
from pytz import timezone
from ask_sdk_s3.adapter import S3Adapter
# s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"])

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.api_client import DefaultApiClient

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import config

contagem_acertos = 2

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        print('ta logando?')
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = '''<speak>
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/eureka_convertido_12s.mp3"/>
        Olá Bedê! Tatá aqui de novo! Verifiquei no Eureka que você está no nível 1 e é um investigador de porão e possui 300 moedas.
        <audio src="soundbank://soundlibrary/cloth_leather_paper/money_coins/money_coins_02"/>
        Vimos que podemos praticar mais no mundo da Matemática. Que acha de continuarmos aquela missão?
        </speak>'''

        question = "Que acha de continuarmos aquela missão?"

        # speak_output = "Olá! Bem vindo ao Eureka!"
        # reprompt_text = "Eu sou Tatá!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(question)
                .response
        )


class EnigmasIntentHandler(AbstractRequestHandler):
    """Handler for Enigmas Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("resolver_enigmas")(handler_input)

    def handle(self, handler_input):       

        speak_output = '''<speak>
        Se prepare que vamos agora entrar no mundo da matemática.
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/eureka_convertido_5s.mp3"/>
        Entrando na missão da Divisibilidade. Prepare-se para desvendar os enigmas que aparecerão nesta missão. 
        Você quer revisar o conteúdo da missão?
        </speak>'''

        question = "Você quer revisar o conteúdo da missão?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(question)
                .response
        )

class PegarEnigmaUmIntentHandler(AbstractRequestHandler):
    """Handler for pegar enigma um Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pegar_enigma_um")(handler_input)

    def handle(self, handler_input):       

        speak_output = '''<speak>
        Então vamos lá…
        <audio src="soundbank://soundlibrary/aircrafts/futuristic/futuristic_02"/>
        Vamos resolver um enigma! ''' +  config.questions['questao1'] + '''</speak>'''

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(config.questions['questao1'])
                .response
        )

class PegarEnigmaDoisIntentHandler(AbstractRequestHandler):
    """Handler for pegar enigma Dois Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pegar_enigma_dois")(handler_input)

    def handle(self, handler_input):      

        speak_output = '''<speak>
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/success_conv.mp3"/>
        <emphasis level="strong">Uau! </emphasis>
        você acertou!
        <break time="1s"/>
        <audio src="soundbank://soundlibrary/aircrafts/futuristic/futuristic_02"/>
        Vamos fazer o 2º enigma! ''' +  config.questions['questao2'] + '''</speak>'''

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(config.questions['questao2'])
                .response
        )

class PegarEnigmaTresErradoIntentHandler(AbstractRequestHandler):
    """Handler for pegar enigma Tres Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pegar_enigma_tres_errado")(handler_input)

    def handle(self, handler_input):  

        speak_output = '''<speak>
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/wrong_conv.mp3"/>
        <emphasis level="reduced">Ops, não foi dessa vez. </emphasis>
        Na próxima vamos conseguir!
        <audio src="soundbank://soundlibrary/aircrafts/futuristic/futuristic_02"/>
        Vamos fazer o 3º enigma! ''' +  config.questions['questao3'] + '''</speak>'''

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(config.questions['questao3'])
                .response
        )


class PegarEnigmaTresCertoIntentHandler(AbstractRequestHandler):
    """Handler for pegar enigma Tres Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pegar_enigma_tres_certo")(handler_input)

    def handle(self, handler_input):   

        global contagem_acertos
        contagem_acertos = 3  

        speak_output = '''<speak>
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/success_conv.mp3"/>
        <emphasis level="strong">Uau! </emphasis>
        você acertou!
        <break time="1s"/>
        <audio src="soundbank://soundlibrary/aircrafts/futuristic/futuristic_02"/>
        Vamos fazer o 3º enigma! ''' +  config.questions['questao3'] + '''</speak>'''

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(config.questions['questao3'])
                .response
        )

class FinalIntentHandler(AbstractRequestHandler):
    """Handler final Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("final_intent")(handler_input)

    def handle(self, handler_input):       

        speak_output = '''<speak>
        <audio src="https://alexathon-group7.s3-sa-east-1.amazonaws.com/success_conv.mp3"/>
        Parabéns! Você acertou.         
        <break time="1s"/>
        Todos os enigmas acabaram. Quer saber como você foi hoje?</speak>'''

        question = "Quer saber como você foi hoje?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(question)
                .response
        )

class ResultadoIntentHandler(AbstractRequestHandler):
    """Handler final Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("resultado_intent")(handler_input)

    def handle(self, handler_input):   

        global contagem_acertos
        contagem_acertos = 2  

        speak_output = '''<speak> Parabéns! Nesta missão, você desvendou <say-as interpret-as="digits">''' + str(contagem_acertos) + '''</say-as> enigmas. Por hoje é só! Até amanhã!</speak>'''

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(question)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Adeus!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, não entendi, pode repetir?."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(api_client=DefaultApiClient())

# sb.add_request_handler(HasBirthdayLaunchRequestHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(EnigmasIntentHandler())
sb.add_request_handler(PegarEnigmaUmIntentHandler())
sb.add_request_handler(PegarEnigmaDoisIntentHandler())

sb.add_request_handler(PegarEnigmaTresErradoIntentHandler())
sb.add_request_handler(PegarEnigmaTresCertoIntentHandler())

sb.add_request_handler(FinalIntentHandler())
sb.add_request_handler(ResultadoIntentHandler())

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()