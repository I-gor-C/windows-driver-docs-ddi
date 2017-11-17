---
UID: NS.wdfcompanion._WDF_COMPANION_EVENT_CALLBACKS
title: WDF_COMPANION_EVENT_CALLBACKS
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_companion_event_callbacks.htm
ms.assetid: 6a9c5420-1847-4145-aea5-9e9c58d86ea1
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WDF_COMPANION_EVENT_CALLBACKS
req.alt-loc: wdfcompanion.h
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
ms.keywords: WDF_COMPANION_EVENT_CALLBACKS, WDF_COMPANION_EVENT_CALLBACKS, *PWDF_COMPANION_EVENT_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_COMPANION_EVENT_CALLBACKS structure



## -description
<p>For internal use only.</p>


## -syntax

````
typedef struct _WDF_COMPANION_EVENT_CALLBACKS {
  ULONG                                   Size;
  PFN_WDF_COMPANION_PRE_D0_ENTRY          EvtCompanionPreD0Entry;
  PFN_WDF_COMPANION_POST_D0_EXIT          EvtCompanionPostD0Exit;
  PFN_WDF_COMPANION_PRE_PREPARE_HARDWARE  EvtCompanionPrePrepareHardware;
  PFN_WDF_COMPANION_POST_RELEASE_HARDWARE EvtCompanionPostReleaseHardware;
} WDF_COMPANION_EVENT_CALLBACKS, *PWDF_COMPANION_EVENT_CALLBACKS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd></dd>

### -field <b>EvtCompanionPreD0Entry</b>

<dd></dd>

### -field <b>EvtCompanionPostD0Exit</b>

<dd></dd>

### -field <b>EvtCompanionPrePrepareHardware</b>

<dd></dd>

### -field <b>EvtCompanionPostReleaseHardware</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
</table>