---
UID: NE.wudfinterrupt._WDF_INTERRUPT_POLARITY
title: WDF_INTERRUPT_POLARITY
author: windows-driver-content
description: The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity.
old-location: wdf\wdf_interrupt_polarity_umdf.htm
old-project: wdf
ms.assetid: 30E61DCE-D88C-47B5-B5CD-3C43C6157FBA
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_INTERRUPT_POLARITY
req.alt-loc: Wudfinterrupt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_POLARITY enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-polarity.md">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify an interrupt signal's polarity.</p>


## -syntax

````
typedef enum _WDF_INTERRUPT_POLARITY { 
  WdfInterruptPolarityUnknown  = 0,
  WdfInterruptActiveHigh       = 1,
  WdfInterruptActiveLow        = 2
} WDF_INTERRUPT_POLARITY, *PWDF_INTERRUPT_POLARITY;
````


## -enum-fields
<dl>

### -field WdfInterruptPolarityUnknown

<dd>
<p>The interrupt signal's polarity is unknown.</p>
</dd>

### -field WdfInterruptActiveHigh

<dd>
<p>The interrupt signal is active when it is high.</p>
</dd>

### -field WdfInterruptActiveLow

<dd>
<p>The interrupt signal is active when it is low.</p>
</dd>
</dl>

## -remarks
<p>The <a href="..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-polarity.md">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify a member of the <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md">WDF_INTERRUPT_INFO</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfinterrupt.h</dt>
</dl>
</td>
</tr>
</table>