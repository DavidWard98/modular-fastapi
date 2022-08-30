import strawberry


@strawberry.type
class Query:
    _hi: str = strawberry.field(resolver=lambda: "Hello GraphQL World!")


schema = strawberry.federation.Schema(query=Query, enable_federation_2=True)
