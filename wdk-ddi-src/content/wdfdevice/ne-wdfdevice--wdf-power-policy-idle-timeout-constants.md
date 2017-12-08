---
UID: NE.wdfdevice._WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS
title: WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS
author: windows-driver-content
description: The WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration is reserved for internal use.
old-location: wdf\wdf_power_policy_idle_timeout_constants.htm
old-project: wdf
ms.assetid: a707c7b9-2fc9-48c8-9492-b911c126668b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 1.9
req.alt-api: WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS
req.alt-loc: wdfdevice.h,wudfddi_types.h
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
req.product: Windows 10 or later.
---

# WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS</b> enumeration is reserved for internal use.</p>


## -syntax

````
typedef enum _WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS { 
  IdleTimeoutDefaultConstant  = 0
} WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS;
````


## -enum-fields
<dl>

### -field IdleTimeoutDefaultConstant

<dd>
<p>For internal use only.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h); </dt>
<dt>Wudfddi_types.h</dt>
</dl>
</td>
</tr>
</table>