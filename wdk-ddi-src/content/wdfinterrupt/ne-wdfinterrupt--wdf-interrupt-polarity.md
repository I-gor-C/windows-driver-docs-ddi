---
UID: NE.wdfinterrupt._WDF_INTERRUPT_POLARITY
title: WDF_INTERRUPT_POLARITY
author: windows-driver-content
description: The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity.
old-location: wdf\wdf_interrupt_polarity.htm
ms.assetid: 6621a1ec-1d4e-4801-9418-d09a0073686a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfinterrupt.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_INTERRUPT_POLARITY
req.alt-loc: wdfinterrupt.h
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
ms.keywords: WDF_COINSTALLER_INSTALL_OPTIONS, WDF_COINSTALLER_INSTALL_OPTIONS, *PWDF_COINSTALLER_INSTALL_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_INTERRUPT_POLARITY enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_INTERRUPT_POLARITY</b> enumeration type is used to specify an interrupt signal's polarity.</p>


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
<p>The <b>WDF_INTERRUPT_POLARITY</b> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

<p>The <b>WDF_INTERRUPT_POLARITY</b> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

<p>The <b>WDF_INTERRUPT_POLARITY</b> enumeration type is used to specify a member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a> structure.</p>

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
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfinterrupt.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464020">WDF_INTERRUPT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_INTERRUPT_POLARITY enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
