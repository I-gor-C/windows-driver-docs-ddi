---
UID: NE.wudfinterrupt._WDF_INTERRUPT_POLARITY
title: WDF_INTERRUPT_POLARITY
author: windows-driver-content
description: The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity.
old-location: wdf\wdf_interrupt_polarity_umdf.htm
ms.assetid: 30E61DCE-D88C-47B5-B5CD-3C43C6157FBA
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
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
ms.keywords: WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_POLARITY enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464028">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify an interrupt signal's polarity.</p>


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

### -field <a id="WdfInterruptPolarityUnknown"></a><a id="wdfinterruptpolarityunknown"></a><a id="WDFINTERRUPTPOLARITYUNKNOWN"></a><b>WdfInterruptPolarityUnknown</b>

<dd>
<p>The interrupt signal's polarity is unknown.</p>
</dd>

### -field <a id="WdfInterruptActiveHigh"></a><a id="wdfinterruptactivehigh"></a><a id="WDFINTERRUPTACTIVEHIGH"></a><b>WdfInterruptActiveHigh</b>

<dd>
<p>The interrupt signal is active when it is high.</p>
</dd>

### -field <a id="WdfInterruptActiveLow"></a><a id="wdfinterruptactivelow"></a><a id="WDFINTERRUPTACTIVELOW"></a><b>WdfInterruptActiveLow</b>

<dd>
<p>The interrupt signal is active when it is low.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464028">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464028">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh464028">WDF_INTERRUPT_POLARITY</a> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

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