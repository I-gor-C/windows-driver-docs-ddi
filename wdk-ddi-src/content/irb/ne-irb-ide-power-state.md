---
UID: NE.irb.IDE_POWER_STATE
title: IDE_POWER_STATE
author: windows-driver-content
description: The IDE_POWER_STATE enumeration type indicates that power state of the device.
old-location: storage\ide_power_state.htm
old-project: storage
ms.assetid: b54655ac-b7ac-4026-9d9d-75dd139ac059
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: WdmlibIoGetAffinityInterrupt
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_POWER_STATE
req.alt-loc: irb.h
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

# IDE_POWER_STATE enumeration



## -description
<p>The IDE_POWER_STATE enumeration type indicates that power state of the device.</p>


## -syntax

````
typedef enum  { 
  IdePowerUnSpecified  = 0,
  IdePowerD0           = 1,
  IdePowerD3           = 2
} IDE_POWER_STATE;
````


## -enum-fields
<dl>

### -field <a id="IdePowerUnSpecified"></a><a id="idepowerunspecified"></a><a id="IDEPOWERUNSPECIFIED"></a><b>IdePowerUnSpecified</b>

<dd>
<p>Indicates that the power level is unspecified.</p>
</dd>

### -field <a id="IdePowerD0"></a><a id="idepowerd0"></a><a id="IDEPOWERD0"></a><b>IdePowerD0</b>

<dd>
<p>Indicates a device power level of 0.</p>
</dd>

### -field <a id="IdePowerD3"></a><a id="idepowerd3"></a><a id="IDEPOWERD3"></a><b>IdePowerD3</b>

<dd>
<p>Indicates a device power level of 3.</p>
</dd>
</dl>

## -remarks
<p>The IDE_POWER_STATE enumeration type is used in conjunction with the <a href="..\irb\nf-irb-ataportrequestpowerstatechange.md">AtaPortRequestPowerStateChange</a> routine to request a power state transition for a device.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\irb\nf-irb-ataportrequestpowerstatechange.md">AtaPortRequestPowerStateChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IDE_POWER_STATE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
