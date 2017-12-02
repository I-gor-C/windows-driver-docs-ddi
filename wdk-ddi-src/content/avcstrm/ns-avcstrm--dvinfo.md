---
UID: NS.avcstrm._DVINFO
title: DVINFO
author: windows-driver-content
description: The DVINFO structure describes a DV stream format including its default streaming source information and stream control information.
old-location: stream\dvinfo.htm
old-project: stream
ms.assetid: 3afd372f-556f-4c3a-804b-9bf7a8c9a438
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: DVINFO, DVINFO, *PDVINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: avcstrm.h
req.include-header: Avcstrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DVINFO
req.alt-loc: avcstrm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# DVINFO structure



## -description
<p>The DVINFO structure describes a DV stream format including its default streaming source information and stream control information.</p>


## -syntax

````
typedef struct _DVINFO {
  DWORD dwDVAAuxSrc;
  DWORD dwDVAAuxCtl;
  DWORD dwDVAAuxSrc1;
  DWORD dwDVAAuxCtl1;
  DWORD dwDVVAuxSrc;
  DWORD dwDVVAuxCtl;
  DWORD dwDVReserved[2];
} DVINFO, *PDVINFO;
````


## -struct-fields
<dl>

### -field dwDVAAuxSrc

<dd>
<p>Specifies the Audio Auxiliary Data Source Pack for the first audio block (first 5 DV DIF sequences for 525-60 systems or 6 DV DIF sequences for 625-50 systems) of a frame. A DIF sequence is a data block that contains 150 DIF blocks. A DIF block consists of 80 bytes. The Audio Auxiliary Data Source Pack is defined in section D.7.1 of Part 2, Annex D, "The Pack Header Table and Contents of Packs" of the <i>Specification of Consumer-use Digital VCRs</i>.</p>
</dd>

### -field dwDVAAuxCtl

<dd>
<p>Specifies the Audio Auxiliary Data Source Control Pack for the first audio block of a frame. The Audio Auxiliary Data Control Pack is defined in section D.7.2 of Part 2, Annex D, "The Pack Header Table and Contents of Packs" of the <i>Specification of Consumer-use Digital VCRs</i>.</p>
</dd>

### -field dwDVAAuxSrc1

<dd>
<p>Specifies the Audio Auxiliary Data Source Pack for the second audio block (second 5 DV DIF sequences for 525-60 systems or 6 DV DIF sequences for 625-50 systems) of a frame.</p>
</dd>

### -field dwDVAAuxCtl1

<dd>
<p>Specifies the Audio Auxiliary Data Source Control Pack for the second audio block of a frame.</p>
</dd>

### -field dwDVVAuxSrc

<dd>
<p>Specifies the Video Auxiliary Data Source Pack as defined in section D.8.1 of Part 2, Annex D, "The Pack Header Table and Contents of Packs" of the <i>Specification of Consumer-use Digital VCRs</i>.</p>
</dd>

### -field dwDVVAuxCtl

<dd>
<p>Specifies the Video Auxiliary Data Source Control Pack as defined in section D.8.2 of Part 2, Annex D, "The Pack Header Table and Contents of Packs" of the <i>Specification of Consumer-use Digital VCRs</i>. </p>
</dd>

### -field dwDVReserved

<dd>
<p>Reserved. This must be set to 0. Do not use this.</p>
</dd>
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
<dt>Avcstrm.h (include Avcstrm.h)</dt>
</dl>
</td>
</tr>
</table>