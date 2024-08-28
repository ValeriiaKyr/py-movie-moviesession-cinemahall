from typing import Union

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:

    session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return session


def get_movies_sessions(
        session_date: Union[str, None] = None
) -> QuerySet[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: Union[str, None] = None,
        movie_id: Union[str, None] = None,
        cinema_hall_id: Union[str, None] = None,
) -> None:
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    session.save()


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    session = MovieSession.objects.get(id=session_id).delete()

    return session
