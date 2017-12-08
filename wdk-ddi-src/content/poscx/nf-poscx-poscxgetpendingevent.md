---
UID: NF.poscx.PosCxGetPendingEvent
title: PosCxGetPendingEvent function
author: windows-driver-content
description: PosCxGetPendingEvent is called either from the device read callback, or when a new event arrives.
old-location: pos\poscxgetpendingevent.htm
old-project: pos
ms.assetid: D68C24E4-DCFB-44F6-92EE-9FF4A1A52841
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxGetPendingEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxGetPendingEvent
req.alt-loc: poscx.h
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
req.product: Windows 10 or later.
---

# PosCxGetPendingEvent function



## -description
      PosCxGetPendingEvent is called either from the device read callback, or when a new 

      event arrives. The function searches the pending events database for events that are waiting for the caller that issued the request.  

      It first searches the control pending events database, and then the data pending event database.


## -syntax

````
NTSTATUS PosCxGetPendingEvent(
  _In_ WDFDEVICE  device,
  _In_ WDFREQUEST request
);
````


## -parameters

### -param device [in]

A handle to a framework device object that represents the device.

### -param request [in]

A handle to a framework request object that represents the read request if <b>PosCxGetPendingEvent</b> is called from the device read callback.

## -returns
Possible return values are:

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Product
</th>
<td width="70%">
Windows 10 or later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>