---
UID: NF.wudfusb.IWDFUsbRequestCompletionParams.GetPipeReadParameters
title: IWDFUsbRequestCompletionParams::GetPipeReadParameters
author: windows-driver-content
description: The GetPipeReadParameters method retrieves parameters that are associated with the completion of a read request.
old-location: wdf\iwdfusbrequestcompletionparams_getpipereadparameters.htm
ms.assetid: e5e3dfa0-49cc-4c2d-828e-fa5c95d3db8c
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfusb.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFUsbRequestCompletionParams.GetPipeReadParameters
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
ms.keywords: IWDFUsbRequestCompletionParams, GetPipeReadParameters, IWDFUsbRequestCompletionParams::GetPipeReadParameters
req.iface: IWDFUsbRequestCompletionParams
req.product: Windows 10 or later.
---

# IWDFUsbRequestCompletionParams::GetPipeReadParameters method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetPipeReadParameters</b> method retrieves parameters that are associated with the completion of a read request.</p>


## -syntax

````
void GetPipeReadParameters(
  [out, optional] IWDFMemory **ppReadMemory,
  [out, optional] SIZE_T     *pBytesRead,
  [out, optional] SIZE_T     *pReadMemoryOffset
);
````


## -parameters
<dl>

### -param <i>ppReadMemory</i> [out, optional]

<dd>
<p>A pointer to a variable that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface, for access to the read buffer for the read request. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>pBytesRead</i> [out, optional]

<dd>
<p>A pointer to a variable that receives the size, in bytes, of the read buffer for the read request. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>pReadMemoryOffset</i> [out, optional]

<dd>
<p>A pointer to a variable that receives the offset, in bytes, into the read buffer for the read request. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


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
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfusb.h (include Wudfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560346">IWDFUsbRequestCompletionParams</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUsbRequestCompletionParams::GetPipeReadParameters method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
