---
UID: NS.nfcradiodev._NFCRM_RADIO_STATE
title: NFCRM_RADIO_STATE
author: windows-driver-content
description: This structure is used to indicate the radio state.
old-location: nfpdrivers\_nfcrm_radio_state_.htm
old-project: nfpdrivers
ms.assetid: 414486ED-464D-4CAF-95C2-9AC59D608816
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: NFCRM_RADIO_STATE, NFCRM_RADIO_STATE, *PNFCRM_RADIO_STATE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: nfcradiodev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NFCRM_RADIO_STATE
req.alt-loc: nfcradiodev.h
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

# NFCRM_RADIO_STATE structure



## -description
<p>This structure is used to indicate the radio state.</p>


## -syntax

````
typedef struct _NFCRM_RADIO_STATE  {
  BOOLEAN MediaRadioOn;
} NFCRM_RADIO_STATE, *PNFCRM_RADIO_STATE;
````


## -struct-fields
<dl>

### -field <b>MediaRadioOn</b>

<dd>
<p>This is a boolean flag that indicates whether the media radio is on.</p>
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
<dt>Nfcradiodev.h</dt>
</dl>
</td>
</tr>
</table>