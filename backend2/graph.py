from langgraph.graph import StateGraph
from backend2.state import TalentState


from backend2.agents.jd_parser import jd_parser
from backend2.agents.matcher import matcher
from backend2.agents.engagement import engagement
from backend2.agents.interest import interest_scorer
from backend2.services.ranking import ranker

def build_graph():

    builder = StateGraph(TalentState)

    builder.add_node("jd_parser", jd_parser)
    builder.add_node("matcher", matcher)
    builder.add_node("engagement", engagement)
    builder.add_node("interest", interest_scorer)
    builder.add_node("ranking", ranker)

    builder.set_entry_point("jd_parser")

    builder.add_edge("jd_parser", "matcher")
    builder.add_edge("matcher", "engagement")
    builder.add_edge("engagement", "interest")
    builder.add_edge("interest", "ranking")

    builder.set_finish_point("ranking")

    return builder.compile()