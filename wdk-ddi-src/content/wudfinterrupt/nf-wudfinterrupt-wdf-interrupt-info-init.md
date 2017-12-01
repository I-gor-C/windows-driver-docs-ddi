---
UID: NF.wudfinterrupt.WDF_INTERRUPT_INFO_INIT
title: WDF_INTERRUPT_INFO_INIT
author: windows-driver-content
description: The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure.
old-location: wdf\wdf_interrupt_info_init_umdf.htm
old-project: wdf
ms.assetid: CFFE19FB-289C-4002-AB07-AE342D855B20
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_INTERRUPT_INFO_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfinterrupt.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WDF_INTERRUPT_INFO_INIT
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

# WDF_INTERRUPT_INFO_INIT function



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md">WDF_INTERRUPT_INFO_INIT</a> function initializes a <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md">WDF_INTERRUPT_INFO</a> structure.</p>


## -syntax

````
VOID WDF_INTERRUPT_INFO_INIT(
  _Out_ PWDF_INTERRUPT_INFO Info
);
````


## -parameters
<dl>

### -param <i>Info</i> [out]

<dd>
<p>A pointer to a driver-allocated <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md">WDF_INTERRUPT_INFO</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md">WDF_INTERRUPT_INFO_INIT</a> function zeros the specified <a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md">WDF_INTERRUPT_INFO</a> structure and sets the structure's <b>Size</b> member.</p>

<p>For more information about handling interrupts in framework-based drivers, see <a href="NULL">Handling Interrupts</a>.</p>

<p>For a code example that uses <a href="..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md">WDF_INTERRUPT_INFO_INIT</a>, see <a href="wdf.iwdfinterrupt_getinfo">IWDFInterrupt::GetInfo</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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

## -see-also
<dl>
<dt>
<a href="..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md">WDF_INTERRUPT_INFO</a>
</dt>
<dt>
<a href="wdf.iwdfinterrupt_getinfo">IWDFInterrupt::GetInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_INFO_INIT function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
