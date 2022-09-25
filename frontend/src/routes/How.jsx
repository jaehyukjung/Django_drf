import styled from "styled-components";
import Nav from "../components/Nav";
import { useNavigate } from 'react-router-dom';

const Background = styled.div`
    width: 100vw;
    height: 100vh;
    background-color: ${props => props.theme.BackColor};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`
const Title = styled.h1`
    color : ${props => props.theme.White};
    font-size:  ${props => props.theme.font};
    font-weight: 700;
    margin-bottom: 40px;
`

const BtnContainer = styled.section`
    display: flex;
    justify-content: space-between;
    width: 450px;
`

const Btn = styled.button`
    border: none;
    width : 200px;
    height: 200px;
    border-radius: 20px;
    box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
    cursor: pointer;
    p{
        font-size: 30px;
        font-weight: 700;
        word-break: keep-all;
    }
    &:active{
        background-color: ${props=>props.theme.Yellow};
        box-shadow: none;
    }
`

const NavCon = styled.div`
    position: absolute;
    top : 10px;
    left : 70px;
`

function How () {
    const navigater = useNavigate();
    const onTouch = () => {
        navigater("/touch");
    }
    const onSound = () => {
        navigater("/sound");
    }

    return(
        <Background>
            <NavCon>
                <Nav />
            </NavCon>
            <Title>
                주문방법  선택
            </Title>
            <BtnContainer>
            <Btn onClick={onTouch} >
                <p>메뉴판에서 선택하기</p>
            </Btn>
            <Btn onClick={onSound }>
                <p>말로 주문하기</p>
            </Btn>
            </BtnContainer>
        </Background>
    )
}

export default How;