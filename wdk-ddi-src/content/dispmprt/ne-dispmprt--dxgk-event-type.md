---
UID: NE.dispmprt._DXGK_EVENT_TYPE
title: DXGK_EVENT_TYPE
author: windows-driver-content
description: The DXGK_EVENT_TYPE enumeration indicates the event type in a call to the display miniport driver's DxgkDdiNotifyAcpiEvent function.
old-location: display\dxgk_event_type.htm
old-project: display
ms.assetid: df28ae8f-01f7-42c5-99df-2a3fc7401173
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_EVENT_TYPE
req.alt-loc: dispmprt.h
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
req.iface: IDebugSystemObjects4
---

# DXGK_EVENT_TYPE enumeration



## -description
<p>The DXGK_EVENT_TYPE enumeration indicates the event type in a call to the display miniport driver's <a href="display.dxgkddinotifyacpievent">DxgkDdiNotifyAcpiEvent</a> function.</p>


## -syntax

````
typedef enum _DXGK_EVENT_TYPE { 
  DxgkUndefinedEvent   = 0,
  DxgkAcpiEvent        = 1,
  DxgkPowerStateEvent  = 2,
  DxgkDockingEvent     = 3
} DXGK_EVENT_TYPE, *PDXGK_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DxgkUndefinedEvent"></a><a id="dxgkundefinedevent"></a><a id="DXGKUNDEFINEDEVENT"></a><b>DxgkUndefinedEvent</b>

<dd>
<p>Indicates that a variable of type DXGK_EVENT_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="DxgkAcpiEvent"></a><a id="dxgkacpievent"></a><a id="DXGKACPIEVENT"></a><b>DxgkAcpiEvent</b>

<dd>
<p>Indicates that the event is an ACPI event.</p>
</dd>

### -field <a id="DxgkPowerStateEvent"></a><a id="dxgkpowerstateevent"></a><a id="DXGKPOWERSTATEEVENT"></a><b>DxgkPowerStateEvent</b>

<dd>
<p>Indicates that the event is a power state event.</p>
</dd>

### -field <a id="DxgkDockingEvent"></a><a id="dxgkdockingevent"></a><a id="DXGKDOCKINGEVENT"></a><b>DxgkDockingEvent</b>

<dd>
<p>Indicates that the event is a docking event.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkddinotifyacpievent">DxgkDdiNotifyAcpiEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_EVENT_TYPE enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
