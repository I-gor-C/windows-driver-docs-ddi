---
UID: NN.wudfusb.IWDFUsbTargetPipe2
title: IWDFUsbTargetPipe2
author: windows-driver-content
description: The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target.
old-location: wdf\iwdfusbtargetpipe2.htm
old-project: wdf
ms.assetid: c3df39cb-17f4-4f68-bde3-f53ba40dde85
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE, WDF_USB_REQUEST_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFUsbTargetPipe2
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
req.product: Windows 10 or later.
---

# IWDFUsbTargetPipe2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]


The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target.



The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFUsbTargetPipe2</b> interface inherits from <a href="..\wudfusb\nn-wudfusb-iwdfusbtargetpipe.md">IWDFUsbTargetPipe</a>. <b>IWDFUsbTargetPipe2</b> also has these types of members:

The <b>IWDFUsbTargetPipe2</b> interface has these methods.

The <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">ConfigureContinuousReader</a> method configures the framework to continuously read from a USB pipe.

 


## -members
The <b>IWDFUsbTargetPipe2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">IWDFUsbTargetPipe2::ConfigureContinuousReader</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">ConfigureContinuousReader</a> method configures the framework to continuously read from a USB pipe.

</td>
</tr>
</table>The <a href="wdf.iwdfusbtargetpipe2_configurecontinuousreader">ConfigureContinuousReader</a> method configures the framework to continuously read from a USB pipe.

 


## -remarks
Drivers obtain the <b>IWDFUsbTargetPipe2</b> interface by calling <b>IWDFUsbTargetPipe::QueryInterface</b>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfusb.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>