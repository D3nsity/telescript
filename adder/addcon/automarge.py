a
    ��`�  �                   @   s�   d dl Z d dlZd dlZeed��Zedddd��.Zejeddd	�Ze�	g d
�� W d  � n1 sf0    Y  e
e�D ]Ze �d� e�d� qxe�d� e �d� dS )�    Nz0In How many accounts you want to add contacts : z../memory.csv�wzUTF-8)�encoding�,�
)Z	delimiterZlineterminator)�   r   �<   z	addcon.py�   �   )�osZcsv�time�int�inputZ
rexaccount�open�file�writerZwriterow�rangeZloop�	startfile�sleep�remove� r   r   �/F:/Telegram/tool2/arsh maan/addcon/automarge.py�<module>   s   ,

