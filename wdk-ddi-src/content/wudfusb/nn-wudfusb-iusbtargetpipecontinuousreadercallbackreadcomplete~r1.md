---
UID: NN.wudfusb.IUsbTargetPipeContinuousReaderCallbackReadComplete~r1
title: IUsbTargetPipeContinuousReaderCallbackReadComplete
author: windows-driver-content
description: IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface.
old-location: wdf\iusbtargetpipecontinuousreadercallbackreadcomplete.htm
old-project: wdf
ms.assetid: 953048ab-872c-4b94-8aef-bcfcb86ea4d8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFUsbTargetPipe2, ConfigureContinuousReader, IWDFUsbTargetPipe2::ConfigureContinuousReader
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfusb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IUsbTargetPipeContinuousReaderCallbackReadComplete
req.alt-loc: wudfusb.h
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
req.iface: IWDFUsbTargetPipe2
req.product: Windows 10 or later.
---

# IUsbTargetPipeContinuousReaderCallbackReadComplete interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
<p><b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> is a driver-supplied interface.</p>
</p>
<p><b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> is a driver-supplied interface.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IUsbTargetPipeContinuousReaderCallbackReadComplete</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> also has these types of members:</p>

<p>The <b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> interface has these methods.</p>

<p>A driver's <a href="wdf.iusbtargetpipecontinuousreadercallbackreadcomplete_onreadercompletion">OnReaderCompletion</a> event callback function informs the driver that a continuous reader has successfully completed a read request.</p>

<p> </p>

## -members
<p>The <b>IUsbTargetPipeContinuousReaderCallbackReadComplete</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iusbtargetpipecontinuousreadercallbackreadcomplete_onreadercompletion">IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion</a>
</td>
<td align="left" width="63%">
<p>A driver's <a href="wdf.iusbtargetpipecontinuousreadercallbackreadcomplete_onreadercompletion">OnReaderCompletion</a> event callback function informs the driver that a continuous reader has successfully completed a read request.</p>
</td>
</tr>
</table><p>A driver's <a href="wdf.iusbtargetpipecontinuousreadercallbackreadcomplete_onreadercompletion">OnReaderCompletion</a> event callback function informs the driver that a continuous reader has successfully completed a read request.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h</dt>
</dl>
</td>
</tr>
</table>