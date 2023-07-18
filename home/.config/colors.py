#! /usr/bin/env python3
import random
esc=""
blackf=f"{esc}[30m"
redf=f"{esc}[31m"
greenf=f"{esc}[32m"
yellowf=f"{esc}[33m"
bluef=f"{esc}[34m"
purplef=f"{esc}[35m"
cyanf=f"{esc}[36m"
whitef=f"{esc}[37m"
blackfbright=f"{esc}[90m"
redfbright=f"{esc}[91m"
greenfbright=f"{esc}[92m"
yellowfbright=f"{esc}[93m"
bluefbright=f"{esc}[94m"
purplefbright=f"{esc}[95m"
cyanfbright=f"{esc}[96m"
whitefbright=f"{esc}[97m"
whitefbright=f"{esc}[97m"  
blackb=f"{esc}[40m"
redb=f"{esc}[41m"
greenb=f"{esc}[42m"
yellowb=f"{esc}[43m"
blueb=f"{esc}[44m"
purpleb=f"{esc}[45m"
cyanb=f"{esc}[46m"
whiteb=f"{esc}[47m"
boldon=f"{esc}[1m"
boldoff=f"{esc}[22m"
italicson=f"{esc}[3m"
italicsoff=f"{esc}[23m"
ulon=f"{esc}[4m"
uloff=f"{esc}[24m"
invon=f"{esc}[7m"
invoff=f"{esc}[27m"
reset=f"{esc}[0m"
clrs = [
  f"""
{boldon}{redfbright}        ■      {boldon}{greenfbright}        ■      {boldon}{yellowfbright}        ■     {boldon}{bluefbright}         ■       {boldon}{purplefbright}       ■      {boldon}{cyanfbright}        ■   {reset}
{boldon}{redfbright}       ■■■     {boldon}{greenfbright}       ■■■     {boldon}{yellowfbright}       ■■■    {boldon}{bluefbright}        ■■■      {boldon}{purplefbright}      ■■■     {boldon}{cyanfbright}       ■■■  {reset}
{boldon}{redfbright}      ■■■■■    {boldon}{greenfbright}      ■■■■■    {boldon}{yellowfbright}      ■■■■■   {boldon}{bluefbright}       ■■■■■     {boldon}{purplefbright}     ■■■■■    {boldon}{cyanfbright}      ■■■■■ {reset}
{redf}     ■(   )■   {greenf}     ■(   )■   {yellowf}     ■(   )■   {bluef}     ■(   )■    {purplef}    ■(   )■   {cyanf}     ■(   )■   {reset}
{redf}    ■■■■ ■■■■  {greenf}    ■■■■ ■■■■  {yellowf}    ■■■■ ■■■■  {bluef}    ■■■■ ■■■■   {purplef}   ■■■■ ■■■■  {cyanf}    ■■■■ ■■■■  {reset}
{redf}   ■■       ■■ {greenf}   ■■       ■■ {yellowf}   ■■       ■■ {bluef}   ■■       ■■  {purplef}  ■■       ■■ {cyanf}   ■■       ■■ {reset}
  """,

  f""" 
{boldon}{redfbright}   ██████  {reset} {boldon}{greenfbright}██████   {reset}{boldon}{yellowfbright}  ██████{reset} {boldon}{bluefbright}██████  {reset} {boldon}{purplefbright}  ██████{reset} {boldon}{cyanfbright}  ███████{reset}
{boldon}{redfbright}   ████████{reset} {boldon}{greenfbright}██    ██ {reset}{boldon}{yellowfbright}██      {reset} {boldon}{bluefbright}██    ██{reset} {boldon}{purplefbright}██████  {reset} {boldon}{cyanfbright}█████████{reset}
{redf}   ██  ████{reset} {greenf}██  ████ {reset}{yellowf}████    {reset} {bluef}████  ██{reset} {purplef}████    {reset} {cyanf}█████    {reset}
{redf}   ██    ██{reset} {greenf}██████   {reset}{yellowf}████████{reset} {bluef}██████  {reset} {purplef}████████{reset} {cyanf}██       {reset} 
  """,

  f"""
{reset}{redf}  ██  ██   {reset}{boldon}{redfbright}██    {reset}{greenf}  ██  ██   {reset}{boldon}{greenfbright}██    {reset}{yellowf}  ██  ██   {reset}{boldon}{yellowfbright}██    {reset}{bluef}  ██  ██   {reset}{boldon}{bluefbright}██    {reset}{purplef}  ██  ██   {reset}{boldon}{purplefbright}██    {reset}{cyanf}  ██  ██   {reset}{boldon}{cyanfbright}██
{reset}{redf}██████████ {reset}{boldon}{redfbright}██    {reset}{greenf}██████████ {reset}{boldon}{greenfbright}██    {reset}{yellowf}██████████ {reset}{boldon}{yellowfbright}██    {reset}{bluef}██████████ {reset}{boldon}{bluefbright}██    {reset}{purplef}██████████ {reset}{boldon}{purplefbright}██    {reset}{cyanf}██████████ {reset}{boldon}{cyanfbright}██
{reset}{redf}  ██  ██   {reset}{boldon}{redfbright}██    {reset}{greenf}  ██  ██   {reset}{boldon}{greenfbright}██    {reset}{yellowf}  ██  ██   {reset}{boldon}{yellowfbright}██    {reset}{bluef}  ██  ██   {reset}{boldon}{bluefbright}██    {reset}{purplef}  ██  ██   {reset}{boldon}{purplefbright}██    {reset}{cyanf}  ██  ██   {reset}{boldon}{cyanfbright}██
{reset}{redf}██████████       {reset}{greenf}██████████       {reset}{yellowf}██████████       {reset}{bluef}██████████       {reset}{purplef}██████████       {reset}{cyanf}██████████   
{reset}{redf}  ██  ██   {reset}{boldon}{redfbright}██    {reset}{greenf}  ██  ██   {reset}{boldon}{greenfbright}██    {reset}{yellowf}  ██  ██   {reset}{boldon}{yellowfbright}██    {reset}{bluef}  ██  ██   {reset}{boldon}{bluefbright}██    {reset}{purplef}  ██  ██   {reset}{boldon}{purplefbright}██    {reset}{cyanf}  ██  ██   {reset}{boldon}{cyanfbright}██ 
{reset}
  """,

  f"""
{reset}{redf}▄█▄█▄ {reset}{boldon}{redfbright}█ {reset}{greenf}▄█▄█▄ {reset}{boldon}{greenfbright}█ {reset}{yellowf}▄█▄█▄ {reset}{boldon}{yellowfbright}█ {reset}{bluef}▄█▄█▄ {reset}{boldon}{bluefbright}█ {reset}{purplef}▄█▄█▄ {reset}{boldon}{purplefbright}█ {reset}{cyanf}▄█▄█▄ {reset}{boldon}{cyanfbright}█{reset} 
{reset}{redf}▄█▄█▄ {reset}{boldon}{redfbright}▀ {reset}{greenf}▄█▄█▄ {reset}{boldon}{greenfbright}▀ {reset}{yellowf}▄█▄█▄ {reset}{boldon}{yellowfbright}▀ {reset}{bluef}▄█▄█▄ {reset}{boldon}{bluefbright}▀ {reset}{purplef}▄█▄█▄ {reset}{boldon}{purplefbright}▀ {reset}{cyanf}▄█▄█▄ {reset}{boldon}{cyanfbright}▀{reset}
{reset}{redf} ▀ ▀  {reset}{boldon}{redfbright}▀ {reset}{greenf} ▀ ▀  {reset}{boldon}{greenfbright}▀ {reset}{yellowf} ▀ ▀  {reset}{boldon}{yellowfbright}▀ {reset}{bluef} ▀ ▀  {reset}{boldon}{bluefbright}▀ {reset}{purplef} ▀ ▀  {reset}{boldon}{purplefbright}▀ {reset}{cyanf} ▀ ▀  {reset}{boldon}{cyanfbright}▀{reset}
  """,

  f"""
{boldon}{whitefbright}    ▄▄▄{reset}
{boldon}{whitefbright} ▄█████▄▄ {reset}
{boldon}{whitefbright}███{cyanb}▀▀▀▀{blackb}▀{cyanb}▀{blackb}▀{cyanb}▀{reset}
{boldon}{whitefbright}███{cyanb}▄   {boldoff}{blackf}▀ ▀{reset}{cyanf}▀{reset}
{boldon}{whitefbright} ▄{cyanb}  {reset}{boldon}{whitefbright}█████▄ {boldoff}{redf}█▄{reset}
{boldoff}{redf}▀▀{reset}{boldon}{redb}{whitefbright}▄{cyanb}▄   {redb}▄▄▄{reset}{boldoff}{redf}▀██▀{reset}
{boldon}{whitefbright} ██▀▀▀██▀  {boldoff}{redf}▀{reset}
{boldon}{whitefbright} ▀▀▀▀ ▀▀▀▀{reset}
  """,

  f"""

{redf}   ▄█████▄ {greenf}   ▄█████▄ {yellowf}   ▄█████▄ {bluef}   ▄█████▄ {purplef}   ▄█████▄ {cyanf}   ▄█████▄
{redf}   █▄▄ ▄▄█ {greenf}   █▄▄ ▄▄█ {yellowf}   █▄▄ ▄▄█ {bluef}   █▄▄ ▄▄█ {purplef}   █▄▄ ▄▄█ {cyanf}   █▄▄ ▄▄█  
{redf}   ███ ███ {greenf}   ███ ███ {yellowf}   ███ ███ {bluef}   ███ ███ {purplef}   ███ ███ {cyanf}   ███ ███  
{redf}   ▀██ ██▀ {greenf}   ▀██ ██▀ {yellowf}   ▀██ ██▀ {bluef}   ▀██ ██▀ {purplef}   ▀██ ██▀ {cyanf}   ▀██ ██▀  
{redf}     ▀ ▀   {greenf}     ▀ ▀   {yellowf}     ▀ ▀   {bluef}     ▀ ▀   {purplef}     ▀ ▀   {cyanf}     ▀ ▀   {reset}
  """,

  f"""
              {reset}{blackf}|               |               |               |               |{reset}
   {redf}█     █{reset}    {blackf}|{reset}    {greenf}█     █{reset}    {blackf}|{reset}    {yellowf}█     █{reset}    {blackf}|{reset}    {bluef}█     █{reset}    {blackf}|{reset}    {purplef}█     █{reset}    {blackf}|{reset}    {cyanf}█     █{reset}
   {redf}███████{reset}    {blackf}|{reset}    {greenf}███████{reset}    {blackf}|{reset}    {yellowf}███████{reset}    {blackf}|{reset}    {bluef}███████{reset}    {blackf}|{reset}    {purplef}███████{reset}    {blackf}|{reset}    {cyanf}███████{reset}
 {redf}███{boldon}{redfbright}██{reset}{redf}█{boldon}{redfbright}██{reset}{redf}███{reset}  {blackf}|{reset}  {greenf}███{boldon}{greenfbright}██{reset}{greenf}█{boldon}{greenfbright}██{reset}{greenf}███{reset}  {blackf}|{reset}  {yellowf}███{boldon}{yellowfbright}██{reset}{yellowf}█{boldon}{yellowfbright}██{reset}{yellowf}███{reset}  {blackf}|{reset}  {bluef}███{boldon}{bluefbright}██{reset}{bluef}█{boldon}{bluefbright}██{reset}{bluef}███{reset}  {blackf}|{reset}  {purplef}███{boldon}{purplefbright}██{reset}{purplef}█{boldon}{purplefbright}██{reset}{purplef}███{reset}  {blackf}|{reset}  {cyanf}███{boldon}{cyanfbright}██{reset}{cyanf}█{boldon}{cyanfbright}██{reset}{cyanf}███{reset}
  {redf}████{boldon}{redfbright}█{reset}{redf}████{reset}   {blackf}|{reset}   {greenf}████{boldon}{greenfbright}█{reset}{greenf}████{reset}   {blackf}|{reset}   {yellowf}████{boldon}{yellowfbright}█{reset}{yellowf}████{reset}   {blackf}|{reset}   {bluef}████{boldon}{bluefbright}█{reset}{bluef}████{reset}   {blackf}|{reset}   {purplef}████{boldon}{purplefbright}█{reset}{purplef}████{reset}   {blackf}|{reset}   {cyanf}████{boldon}{cyanfbright}█{reset}{cyanf}████{reset}
  {redf}█ █ {boldon}{redfbright}█{reset} {redf}█ █{reset}   {blackf}|{reset}   {greenf}█ █ {boldon}{greenfbright}█{reset} {greenf}█ █{reset}   {blackf}|{reset}   {yellowf}█ █ {boldon}{yellowfbright}█{reset} {yellowf}█ █{reset}   {blackf}|{reset}   {bluef}█ █ {boldon}{bluefbright}█{reset} {bluef}█ █{reset}   {blackf}|{reset}   {purplef}█ █ {boldon}{purplefbright}█{reset} {purplef}█ █{reset}   {blackf}|{reset}   {cyanf}█ █ {boldon}{cyanfbright}█{reset} {cyanf}█ █{reset}
    {redf}█   █{reset}     {blackf}|{reset}     {greenf}█   █{reset}     {blackf}|{reset}     {yellowf}█   █{reset}     {blackf}|{reset}     {bluef}█   █{reset}     {blackf}|{reset}     {purplef}█   █{reset}     {blackf}|{reset}     {cyanf}█   █{reset}
              {blackf}|               |               |               |               |{reset}
  """,
  f"""

    {boldon}{blackf} ██████{reset}
   {boldon}{blackf}██{reset}██{reset}{bluef}██{reset}{boldon}{blackf}██{reset}{bluef}██{reset}
   {boldon}{blackf}██{reset}██{bluef}██{reset}{boldon}{blackf}██{reset}{bluef}██{reset}
   {boldon}{blackf}██████{reset}{purplef}██████{reset}
   {boldon}{blackf}████{reset}████{boldon}{blackf}██{reset}
 {boldon}{blackf}████{reset}████████{boldon}{blackf}██{reset}
 {boldon}{blackf}████{reset}████████{boldon}{blackf}██{reset}
 {boldon}{blackf}████{reset}████████{boldon}{blackf}██{reset}
   {boldon}{blackf}████{reset}████{boldon}{blackf}██{reset}
  {boldon}{blackf}███{reset}{purplef}███   ████{reset}
  """,

  f"""
 {redf}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗  {greenf}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗  {yellowf}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
 {boldon}{redfbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝  {greenfbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝  {yellowfbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝{reset}
  ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
 {bluef}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗  {purplef}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗  {cyanf}╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗
 {boldon}{bluefbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝  {purplefbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝  {cyanfbright}╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝{reset}
  """,
  f"""
 {redf}▀ █{reset} {boldon}{redfbright}█ ▀{reset}   {greenf}▀ █{reset} {boldon}{greenfbright}█ ▀{reset}   {yellowf}▀ █{reset} {boldon}{yellowfbright}█ ▀{reset}   {bluef}▀ █{reset} {boldon}{bluefbright}█ ▀{reset}   {purplef}▀ █{reset} {boldon}{purplefbright}█ ▀{reset}   {cyanf}▀ █{reset} {boldon}{cyanfbright}█ ▀{reset} 
 {redf}██{reset}  {boldon}{redfbright} ██{reset}   {greenf}██{reset}   {boldon}{greenfbright}██{reset}   {yellowf}██{reset}   {boldon}{yellowfbright}██{reset}   {bluef}██{reset}   {boldon}{bluefbright}██{reset}   {purplef}██{reset}   {boldon}{purplefbright}██{reset}   {cyanf}██{reset}   {boldon}{cyanfbright}██{reset}  
 {redf}▄ █{reset}{boldon}{redfbright} █ ▄ {reset}  {greenf}▄ █ {reset}{boldon}{greenfbright}█ ▄{reset}   {yellowf}▄ █ {reset}{boldon}{yellowfbright}█ ▄{reset}   {bluef}▄ █ {reset}{boldon}{bluefbright}█ ▄{reset}   {purplef}▄ █ {reset}{boldon}{purplefbright}█ ▄{reset}   {cyanf}▄ █ {reset}{boldon}{cyanfbright}█ ▄{reset}  
  """,

  f"""
  {boldon}{redfbright}    █    {reset}    {boldon}{greenfbright}    █    {reset}    {boldon}{yellowfbright}    █    {reset}    {boldon}{bluefbright}    █    {reset}    {boldon}{purplefbright}    █    {reset}    {boldon}{cyanfbright}    █    {reset}
  {boldon}{redfbright}▄▄  █  ▄▄{reset}    {boldon}{greenfbright}▄▄  █  ▄▄{reset}    {boldon}{yellowfbright}▄▄  █  ▄▄{reset}    {boldon}{bluefbright}▄▄  █  ▄▄{reset}    {boldon}{purplefbright}▄▄  █  ▄▄{reset}    {boldon}{cyanfbright}▄▄  █  ▄▄{reset}
  {boldon}{redfbright}███▀▀▀███{reset}    {boldon}{greenfbright}███▀▀▀███{reset}    {boldon}{yellowfbright}███▀▀▀███{reset}    {boldon}{bluefbright}███▀▀▀███{reset}    {boldon}{purplefbright}███▀▀▀███{reset}    {boldon}{cyanfbright}███▀▀▀███{reset}
  {boldon}{redfbright}███ █ ███{reset}    {boldon}{greenfbright}███ █ ███{reset}    {boldon}{yellowfbright}███ █ ███{reset}    {boldon}{bluefbright}███ █ ███{reset}    {boldon}{purplefbright}███ █ ███{reset}    {boldon}{cyanfbright}███ █ ███{reset}
  {boldon}{redfbright}██ ▀▀▀ ██{reset}    {boldon}{greenfbright}██ ▀▀▀ ██{reset}    {boldon}{yellowfbright}██ ▀▀▀ ██{reset}    {boldon}{bluefbright}██ ▀▀▀ ██{reset}    {boldon}{purplefbright}██ ▀▀▀ ██{reset}    {boldon}{cyanfbright}██ ▀▀▀ ██{reset}
  """,

  f"""
 {redf} ▄█▀ █ █ ▀█▄   {greenf} ▄█▀ █ █ ▀█▄   {yellowf} ▄█▀ █ █ ▀█▄   {bluef} ▄█▀ █ █ ▀█▄   {purplef} ▄█▀ █ █ ▀█▄   {cyanf} ▄█▀ █ █ ▀█▄ 
 {redf}███  ███  ███  {greenf}███  ███  ███  {yellowf}███  ███  ███  {bluef}███  ███  ███  {purplef}███  ███  ███  {cyanf}███  ███  ███
 {redf}█████████████  {greenf}█████████████  {yellowf}█████████████  {bluef}█████████████  {purplef}█████████████  {cyanf}█████████████
 {redf} ▀██▄   ▄██▀   {greenf} ▀██▄   ▄██▀   {yellowf} ▀██▄   ▄██▀   {bluef} ▀██▄   ▄██▀   {purplef} ▀██▄   ▄██▀   {cyanf} ▀██▄   ▄██▀ 
{reset} 
""",
  f"""
{redf}   ▄█     █▄    {greenf}   ▄▄     ▄▄    {yellowf}   ▄▄     ▄▄    {bluef}   ▄▄     ▄▄    {purplef}   ▄▄     ▄▄    {cyanf}   ▄█     █▄   
{redf} ▄█▀  ▄▄▄  ▀█▄  {greenf} ▄█▀  ▄▄▄  ▀█▄  {yellowf} ▄█▀  ▄▄▄  ▀█▄  {bluef} ▄█▀  ▄▄▄  ▀█▄  {purplef} ▄█▀  ▄▄▄  ▀█▄  {cyanf} ▄█▀  ▄▄▄  ▀█▄ 
{redf} ██▄▄██▀██▄▄██  {greenf} ██▄▄██▀██▄▄██  {yellowf} ██▄▄██▀██▄▄██  {bluef} ██▄▄██▀██▄▄██  {purplef} ██▄▄██▀██▄▄██  {cyanf} ██▄▄██▀██▄▄██ 
{redf} ██▀▀█████▀▀██  {greenf} ██▀▀█████▀▀██  {yellowf} ██▀▀█████▀▀██  {bluef} ██▀▀█████▀▀██  {purplef} ██▀▀█████▀▀██  {cyanf} ██▀▀█████▀▀██ 
{redf} ▀█▄  ▀▀▀  ▄█▀  {greenf} ▀█▄  ▀▀▀  ▄█▀  {yellowf} ▀█▄  ▀▀▀  ▄█▀  {bluef} ▀█▄  ▀▀▀  ▄█▀  {purplef} ▀█▄  ▀▀▀  ▄█▀  {cyanf} ▀█▄  ▀▀▀  ▄█▀ 
{redf}   ▀█     █▀    {greenf}   ▀▀     ▀▀    {yellowf}   ▀▀     ▀▀    {bluef}   ▀▀     ▀▀    {purplef}   ▀▀     ▀▀    {cyanf}   ▀█     █▀   
{reset}""",

  f"""
{redf}    ▄▄▄      {greenf}    ▄▄▄      {yellowf}    ▄▄▄      {bluef}    ▄▄▄      {purplef}    ▄▄▄      {cyanf}    ▄▄▄     
{redf}   ▀█▀██  ▄  {greenf}   ▀█▀██  ▄  {yellowf}   ▀█▀██  ▄  {bluef}   ▀█▀██  ▄  {purplef}   ▀█▀██  ▄  {cyanf}   ▀█▀██  ▄ 
{redf} ▀▄██████▀   {greenf} ▀▄██████▀   {yellowf} ▀▄██████▀   {bluef} ▀▄██████▀   {purplef} ▀▄██████▀   {cyanf} ▀▄██████▀  
{redf}    ▀█████   {greenf}    ▀█████   {yellowf}    ▀█████   {bluef}    ▀█████   {purplef}    ▀█████   {cyanf}    ▀█████  
{redf}       ▀▀▀▀▄ {greenf}       ▀▀▀▀▄ {yellowf}       ▀▀▀▀▄ {bluef}       ▀▀▀▀▄ {purplef}       ▀▀▀▀▄ {cyanf}       ▀▀▀▀▄
{reset}""",
  f"""
 {yellowf}  ▄███████▄                {redf}  ▄██████▄    {greenf}  ▄██████▄    {bluef}  ▄██████▄    {purplef}  ▄██████▄    {cyanf}  ▄██████▄    
 {yellowf}▄█████████▀▀               {redf}▄{whitef}█▀█{redf}██{whitef}█▀█{redf}██▄  {greenf}▄█{whitef}███{greenf}██{whitef}███{greenf}█▄  {bluef}▄█{whitef}███{bluef}██{whitef}███{bluef}█▄  {purplef}▄█{whitef}███{purplef}██{whitef}███{purplef}█▄  {cyanf}▄██{whitef}█▀█{cyanf}██{whitef}█▀█{cyanf}▄
 {yellowf}███████▀      {whitef}▄▄  ▄▄  ▄▄   {redf}█{whitef}▄▄█{redf}██{whitef}▄▄█{redf}███  {greenf}██{whitef}█ █{greenf}██{whitef}█ █{greenf}██  {bluef}██{whitef}█ █{bluef}██{whitef}█ █{bluef}██  {purplef}██{whitef}█ █{purplef}██{whitef}█ █{purplef}██  {cyanf}███{whitef}█▄▄{cyanf}██{whitef}█▄▄{cyanf}█
 {yellowf}███████▄      {whitef}▀▀  ▀▀  ▀▀   {redf}████████████  {greenf}████████████  {bluef}████████████  {purplef}████████████  {cyanf}████████████  
 {yellowf}▀█████████▄▄               {redf}██▀██▀▀██▀██  {greenf}██▀██▀▀██▀██  {bluef}██▀██▀▀██▀██  {purplef}██▀██▀▀██▀██  {cyanf}██▀██▀▀██▀██
 {yellowf}  ▀███████▀                {redf}▀   ▀  ▀   ▀  {greenf}▀   ▀  ▀   ▀  {bluef}▀   ▀  ▀   ▀  {purplef}▀   ▀  ▀   ▀  {cyanf}▀   ▀  ▀   ▀ {reset}
  """,

  f"""
{redf}▬▬▬▬▬ {greenf}▬▬▬▬▬ {yellowf}▬▬▬▬▬ {bluef}▬▬▬▬▬ {purplef}▬▬▬▬▬ {cyanf}▬▬▬▬▬
{redf}▬▬▬▬▬ {greenf}▬▬▬▬▬ {yellowf}▬▬▬▬▬ {bluef}▬▬▬▬▬ {purplef}▬▬▬▬▬ {cyanf}▬▬▬▬▬ {reset}
  """,
  f"""
{redf}▀■▄ {greenf}▀■▄ {yellowf}▀■▄ {bluef}▀■▄ {purplef}▀■▄ {cyanf}▀■▄
{redf}▀■▄ {greenf}▀■▄ {yellowf}▀■▄ {bluef}▀■▄ {purplef}▀■▄ {cyanf}▀■▄ {reset}
"""
]

print(random.choice(clrs))
