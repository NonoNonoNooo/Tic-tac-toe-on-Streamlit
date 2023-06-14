'''Tic-tac-toe on Streamlit'''
import streamlit as st
import time


if 'count' not in st.session_state:
    st.session_state['count'] = 1

if 'board' not in st.session_state:
    st.session_state['board'] = list(range(1, 10))

if 'who_win' not in st.session_state:
    st.session_state['who_win'] = ''

if 'player_1' not in st.session_state:
    st.session_state['player_1'] = 0

if 'player_2' not in st.session_state:
    st.session_state['player_2'] = 0


def chec_win(board):
    win_cord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for each in win_cord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

style = '''
<style>
input {
  text-align: center;
}
</style>
'''

def main():
    st.markdown(style, unsafe_allow_html=True)


    st.markdown(
        '''
        <div style="text-align: center; color: white;">
            <h1 style="text-align: center;">Tic-tac-toe on Streamlit</h1>
        </div>
        ''', unsafe_allow_html=True
    )


    input_ = st.text_input('Move',max_chars=1)


    if input_:
        if input_ in '123456789':
            if st.session_state['count'] % 2 !=0:
                if str(st.session_state['board'][int(input_) - 1]) not in 'XO':
                    st.session_state['board'][int(input_) - 1] = 'X'
                    st.session_state['count'] += 1
            else:
                if str(st.session_state['board'][int(input_) - 1]) not in 'XO':
                    st.session_state['board'][int(input_) - 1] = 'O'
                    st.session_state['count'] += 1

            if st.session_state['count']-1 > 4:
                tmp = chec_win(st.session_state['board'])
                if tmp:
                    st.session_state['who_win'] = 'Won by ' + tmp
                    if tmp == 'X':
                        st.session_state['player_1'] += 1
                    else:
                        st.session_state['player_2'] += 1

                    st.session_state['count'] = 1
                    st.session_state['board'] = list(range(1, 10))


                if st.session_state['count']-1 == 9:
                    st.session_state['who_win'] = 'Draw'

                    st.session_state['count'] = 1
                    st.session_state['board'] = list(range(1, 10))
        else:
            st.text('Please enter a number')


    st.markdown(
        f'''
        <div style="text-align: center; color: white;">
            <h5 style="text-align: center;">{"Player 1's move 'X'" if st.session_state['count'] % 2 != 0 else "Player 2's move 'X'"}</h5>
            <h6 style="text-align: center;">{st.session_state['who_win']}</h6>
            <h6 style="text-align: center;">Player 1: Player 2</h6>
            <h6 style="text-align: center;">{st.session_state['player_1']} : {st.session_state['player_2']}</h6>
        </div>
        ''', unsafe_allow_html=True
    )


    st.markdown(
        f"""
            <div class="game-board" id="game-board" style="display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr); gap: 5px; width: 500px; height: 500px; margin: 0 auto; background-color: #e0e0e0; padding: 5px;">
                <div class="game-cell" onclick="makeMove(0)" id="cell-0" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][0]}</div>
                <div class="game-cell" onclick="makeMove(1)" id="cell-1" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][1]}</div>
                <div class="game-cell" onclick="makeMove(2)" id="cell-2" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][2]}</div>
                <div class="game-cell" onclick="makeMove(3)" id="cell-3" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][3]}</div>
                <div class="game-cell" onclick="makeMove(4)" id="cell-4" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][4]}</div>
                <div class="game-cell" onclick="makeMove(5)" id="cell-5" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][5]}</div>
                <div class="game-cell" onclick="makeMove(6)" id="cell-6" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][6]}</div>
                <div class="game-cell" onclick="makeMove(7)" id="cell-7" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][7]}</div>
                <div class="game-cell" onclick="makeMove(8)" id="cell-8" style="display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: bold; background-color: rgb(14, 17, 23); cursor: pointer;">{st.session_state['board'][8]}</div>
            </div>
        """,
        unsafe_allow_html=True
    )

    if st.session_state['who_win'] != '':
        time.sleep(3)
        st.session_state['who_win'] = ''

if __name__ == '__main__':
    main()

