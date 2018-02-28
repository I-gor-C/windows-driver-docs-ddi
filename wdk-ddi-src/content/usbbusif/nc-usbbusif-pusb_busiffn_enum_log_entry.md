---
UID: NC:usbbusif.PUSB_BUSIFFN_ENUM_LOG_ENTRY
title: USB_BUSIFFN_ENUM_LOG_ENTRY
author: windows-driver-content
description: This callback function is not supported.The EnumLogEntry routine makes a log entry.
old-location: buses\enumlogentry.htm
old-project: usbref
ms.assetid: 6c7f1ab6-bbd8-45d8-92af-030db336c97c
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: EnumLogEntry, EnumLogEntry callback function [Buses], USB_BUSIFFN_ENUM_LOG_ENTRY, buses.enumlogentry, usbbusif/EnumLogEntry, usbinterKR_a05ba50b-df81-4211-918b-e7409bc1d5ff.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbbusif.h
req.include-header: Usbbusif.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: ANY
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	usbbusif.h
api_name:
-	EnumLogEntry
product: Windows
targetos: Windows
req.typenames: USBD_VERSION_INFORMATION, *PUSBD_VERSION_INFORMATION
req.product: Windows 10 or later.
---


# PUSB_BUSIFFN_ENUM_LOG_ENTRY callback function
This callback function is not supported.

The <i>EnumLogEntry</i> routine makes a log entry.

## Syntax

```
PUSB_BUSIFFN_ENUM_LOG_ENTRY PusbBusiffnEnumLogEntry;

NTSTATUS PusbBusiffnEnumLogEntry(
  PVOID ,
  ULONG ,
  ULONG ,
  ULONG ,
  ULONG 
)
{...}
```

## Parameters

`Arg1`



`Arg1`



`Arg1`



`Arg1`



`Arg1`




## Return Value

The <i>EnumLogEntry </i>routine always returns STATUS_SUCCESS.

## Remarks

The routine definition that is provided on this reference page is an example routine whose parameters are just placeholder names. The actual prototype of the routine is declared in <i>usbbusif.h</i> as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef NTSTATUS
  (USB_BUSIFFN *PUSB_BUSIFFN_ENUM_LOG_ENTRY) (
    IN PVOID,
    IN ULONG,
    IN ULONG,
    IN ULONG,
    IN ULONG
);</pre>
</td>
</tr>
</table></span></div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | usbbusif.h (include Usbbusif.h) |
| **IRQL** | ANY |