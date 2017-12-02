---
UID: NS.smclib._PTS_DATA
title: PTS_DATA
author: windows-driver-content
description: The PTS_DATA structure is used for protocol type selection (PTS).
old-location: smartcrd\pts_data.htm
old-project: smartcrd
ms.assetid: aa542c6f-24f9-4ef4-a425-93905cca976a
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: PTS_DATA, PTS_DATA, *PPTS_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PTS_DATA
req.alt-loc: smclib.h
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
req.product: Windows 10 or later.
---

# PTS_DATA structure



## -description
<p>The PTS_DATA structure is used for protocol type selection (PTS).</p>


## -syntax

````
typedef struct _PTS_DATA {
  UCHAR Type;
  UCHAR Fl;
  UCHAR Dl;
  ULONG CLKFrequency;
  ULONG DataRate;
  UCHAR StopBits;
} PTS_DATA, *PPTS_DATA;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>Controls how the remaining members of this structure are calculated. This member can have one of the following values:</p>
<p></p>
<dl>

### -field PTS_TYPE_DEFAULT

<dd>
<p>Calculates standard parameters for PTS.</p>
</dd>

### -field PTS_TYPE_OPTIMAL

<dd>
<p>Calculates the best possible parameters for PTS.</p>
</dd>

### -field PTS_TYPE_USER

<dd>
<p>Calculates user-defined parameters for PTS.</p>
<p>The smart card driver library populates the remaining members of this structure when the reader driver calls its <a href="https://msdn.microsoft.com/library/windows/hardware/ff548972">SmartcardUpdateCardCapabilities (WDM)</a> routine. However, in some cases, the reader driver might be responsible for setting these parameters. For example, if a PTS request that specifies optimal parameters fails, the reader driver can set the parameters in a callback function that specifies the protocol. To specify the protocol, the callback function should set the type to PTS_TYPE_DEFAULT and call <b>SmartcardUpdateCardCapabilities</b> again. </p>
</dd>
</dl>
</dd>

### -field Fl

<dd>
<p>The Fl value to use as part of PTS1 for the PTS request.</p>
</dd>

### -field Dl

<dd>
<p>The Dl value to use as part of PTS1 for the PTS request.</p>
</dd>

### -field CLKFrequency

<dd>
<p>Contains the clock frequency. Some smart card readers must be programmed by using the new clock frequency to use after the PTS request.</p>
</dd>

### -field DataRate

<dd>
<p>Contains the new data rate. Some smart card readers (for example, serial readers) must be set to the new data rate to use after a PTS request.</p>
</dd>

### -field StopBits

<dd>
<p>Contains the number of stop bits to use with the inserted card.</p>
</dd>
</dl>

## -remarks
<p>The smart card reader driver library assigns values to the members of this structure before it calls the callback function that sets the protocol. The driver library considers the characteristics of the inserted smart card, the supported clock frequencies, and supported data rates of the reader when it assigns the values. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>