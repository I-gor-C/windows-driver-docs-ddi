---
UID: NS.bdatypes._BDA_DVBT2_L1_SIGNALLING_DATA
title: BDA_DVBT2_L1_SIGNALLING_DATA
author: windows-driver-content
description: .
old-location: stream\bda_dvbt2_l1_signalling_data.htm
old-project: stream
ms.assetid: 34BD68C3-446A-4074-8F5C-E670BE09083A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_DVBT2_L1_SIGNALLING_DATA, BDA_DVBT2_L1_SIGNALLING_DATA, *PBDA_DVBT2_L1_SIGNALLING_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_DVBT2_L1_SIGNALLING_DATA
req.alt-loc: Bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDA_DVBT2_L1_SIGNALLING_DATA structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_DVBT2_L1_SIGNALLING_DATA {
  BYTE L1Pre_TYPE;
  BYTE L1Pre_BWT_S1_S2;
  BYTE L1Pre_REPETITION_GUARD_PAPR;
  BYTE L1Pre_MOD_COD_FEC;
  BYTE L1Pre_POSTSIZE_INFO_PILOT[5];
  BYTE L1Pre_TX_ID_AVAIL;
  BYTE L1Pre_CELL_ID[2];
  BYTE L1Pre_NETWORK_ID[2];
  BYTE L1Pre_T2SYSTEM_ID[2];
  BYTE L1Pre_NUM_T2_FRAMES;
  BYTE L1Pre_NUM_DATA_REGENFLAG_L1POSTEXT[2];
  BYTE L1Pre_NUMRF_CURRENTRF_RESERVED[2];
  BYTE L1Pre_CRC32[4];
  BYTE L1PostData[MIN_DIMENSION];
} BDA_DVBT2_L1_SIGNALLING_DATA, *PBDA_DVBT2_L1_SIGNALLING_DATA;
````


## -struct-fields
<dl>

### -field L1Pre_TYPE

<dd></dd>

### -field L1Pre_BWT_S1_S2

<dd></dd>

### -field L1Pre_REPETITION_GUARD_PAPR

<dd></dd>

### -field L1Pre_MOD_COD_FEC

<dd></dd>

### -field L1Pre_POSTSIZE_INFO_PILOT

<dd></dd>

### -field L1Pre_TX_ID_AVAIL

<dd></dd>

### -field L1Pre_CELL_ID

<dd></dd>

### -field L1Pre_NETWORK_ID

<dd></dd>

### -field L1Pre_T2SYSTEM_ID

<dd></dd>

### -field L1Pre_NUM_T2_FRAMES

<dd></dd>

### -field L1Pre_NUM_DATA_REGENFLAG_L1POSTEXT

<dd></dd>

### -field L1Pre_NUMRF_CURRENTRF_RESERVED

<dd></dd>

### -field L1Pre_CRC32

<dd></dd>

### -field L1PostData

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>