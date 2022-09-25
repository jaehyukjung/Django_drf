import styled from "styled-components";
import Nav from '../components/Nav';
import img from "../mainC.png"
import mic from "../disM.png"
import ymic from "../isM.png"
import { useState, useEffect } from "react";
import { useSpeechRecognition } from 'react-speech-kit';

const NavCon = styled.div`
    position: absolute;
    top : 10px;
    left : 70px;
`
const Img = styled.img`
    width: ${props => props.theme.swh};
    height: ${props => props.theme.swh};
`
const Title = styled.h1`
    color : ${props => props.theme.White};
    font-size:  ${props => props.theme.font2};
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
`

const Background = styled.div`
    width: 100vw;
    height: 100vh;
    background-color: ${props => props.theme.BackColor};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`
const MicImg = styled.img`
    width: ${props => props.theme.mwh};
    height: ${props => props.theme.mwh};
    cursor: pointer;
`

const YMicImg = styled.img`
    width: 180px;
    height: 180px;
`

const ImgContain = styled.div`
    display: flex;
    align-items: center;
`

function Sound() {
    const [value, setValue] = useState('');
    const [list, setList] = useState([]);
    const { listen, listening, stop } = useSpeechRecognition({
    onResult: (result) => {
        setValue(result);
    },
    });
    useEffect(() => {
        setList((prev) => {
            return [...prev, value]
        })
    },[value])

    console.log(list);
    return(
        <Background>
            <NavCon>
                <Nav />
            </NavCon>
            <Img src={img} />
            <Title>
                {listening ? `듣는 중입니다${value}` : <ImgContain><MicImg style={{width : "30px", height : "30px"}} src={mic} />을 누른 후, 원하는 메뉴를 말씀해주세요!</ImgContain>}
            </Title>
                {listening ? <YMicImg onClick={stop} src={ymic} />  : <MicImg onClick={listen} src={mic} />}
        </Background>
    )
}

export default Sound;