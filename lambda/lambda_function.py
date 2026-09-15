# -*- coding: utf-8 -*-
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler, AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

sb = SkillBuilder()


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech = "Ciao. Chiedi: quando passa il bus per scuola."
        return handler_input.response_builder.speak(speech).ask(speech).response


class ProssimoBusScuolaHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ProssimoBusScuolaIntent")(handler_input)

    def handle(self, handler_input):
        speech = "La skill funziona. La ricerca del prossimo autobus verra aggiunta dopo."
        return handler_input.response_builder.speak(speech).response


class HelpHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech = "Puoi chiedere: quando passa il bus per scuola."
        return handler_input.response_builder.speak(speech).ask(speech).response


class CancelStopHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            is_intent_name("AMAZON.CancelIntent")(handler_input)
            or is_intent_name("AMAZON.StopIntent")(handler_input)
        )

    def handle(self, handler_input):
        return handler_input.response_builder.speak("Alla prossima.").response


class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        return handler_input.response_builder.speak("Si e verificato un problema. Riprova tra poco.").response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(ProssimoBusScuolaHandler())
sb.add_request_handler(HelpHandler())
sb.add_request_handler(CancelStopHandler())
sb.add_exception_handler(AllExceptionHandler())

handler = sb.lambda_handler()
