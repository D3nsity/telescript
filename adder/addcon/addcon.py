a
    ڭ�`k  �                   @   s�  d dl mZ d dlmZmZ d dl mZ d dlmZ d dlmZm	Z	m
Z
mZ d dlmZmZmZmZ d dlmZ d dlmZmZ d dlmZmZmZ d d	lZd d	lZd d	lZd d
lmZ d d	lZd d	lZd d	lZedd��<Zee�Z e!e �Z"dZ#dZ$e"e#d  e$d  Z%W d	  � n1 �s0    Y  e&e%�Z'e'd a(edd��<Z)ee)�Z e!e �Z"e'Z#dZ$e"e#d  e$d  Z*W d	  � n1 �s�0    Y  e*Z+dd� Z,e,�  d	S )�    )�TelegramClient)�	functions�types)�GetDialogsRequest)�InputPeerEmpty�InputPeerChannel�InputPeerUser�PeerUser)�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantError)�InviteToChannelRequest)�GetFullChannelRequest�JoinChannelRequest)r   �utils�errorsN)�reader�../memory.csv�r�   z../phone.csvc                  C   s�  t �t�} td| � �dd�}|��  |�� sNtd� |�| � |�| t	d�� d}g }t
|dd��v}tj|d	d
d�}t|d � |D ]F}i }|d |d< |d |d< t|d �|d< |d |d< |�|� q�W d   � n1 s�0    Y  t
dd��<}t|�}	t|	�}
d}d}|
|d  |d  }W d   � n1 �s60    Y  t|�}|d }t
dd��<}t|�}	t|	�}
d}d}|
|d  |d  }W d   � n1 �s�0    Y  t|�}|d }t
dddd��0}tj|d	d
d�}|�t||g� W d   � n1 �s�0    Y  |D �]�}t|�t|d �k�r�t|d �t|�k�r�z\d}|d dk�r`td� W �q|tjj|d |d dddd�� d}t�t�dd�� W n� t�y�   d}Y n� t�y�   d }Y n� t�y } z"d!}td"� t�d#� W Y d }~n�d }~0  tj�y0 } z|j j!}W Y d }~nRd }~0  t"�yX } z|}W Y d }~n*d }~0    t#�$�  td$� Y �qY n0 td%|� d&�� n$t|d �t|�k�rtd'� t%�  �qd S )(Nz../sessions/i�$ Z 7e14b38d250953c8c1e94fd7b2d63550zsome thing has changedzEnter the code: z../data.csvzUTF-8)�encoding�,�
)Z	delimiterZlineterminatorr   Zsrnor   Zusername�   �id�   �namer   r   �<   �w�LEGEND� zno username, moving to nextT)r   Z
first_name�	last_name�phoneZadd_phone_privacy_exceptionZDONE�   ZPrivacyRestrictedErrorZALREADYzPeerFloodError :(r
   i�Q zUnexpected ErrorzADDED > � z'Members Added To Contact. Successfully!)&r   Zparse_phone�pphoner   ZconnectZis_user_authorized�printZsend_code_requestZsign_in�input�open�csvr   �next�int�append�list�writerZwriterow�
nextLEGENDr   ZcontactsZAddContactRequest�time�sleep�randomZ	randranger   r   r
   r   ZRPCError�	__class__�__name__�	Exception�	traceback�	print_exc�quit)r#   ZclientZ
input_fileZusers�fZrows�row�user�hash_obj�
csv_reader�list_of_rows�
row_number�
col_numberZnumnextZ	startfromZ	nextstartZnumendZendtoZnextendZdfr/   Zstatus�g�e�d� rE   �,F:/Telegram/tool2/arsh maan/addcon/addcon.py�autos*   s�    


*440
,�rG   )-Ztelethon.syncr   Ztelethonr   r   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   r   r   r	   Ztelethon.errors.rpcerrorlistr
   r   r   r   Ztelethon.tl.functions.channelsr   r   r   r   r   Zconfigparser�sysr*   r   r7   r1   r3   r)   r=   r>   r.   r?   r@   rA   Znumdelr,   r    r0   Zread_obj�valuer&   rG   rE   rE   rE   rF   �<module>   s@   44i