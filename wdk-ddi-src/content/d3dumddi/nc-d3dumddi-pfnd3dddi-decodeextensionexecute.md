---
UID: NC.d3dumddi.PFND3DDDI_DECODEEXTENSIONEXECUTE
title: PFND3DDDI_DECODEEXTENSIONEXECUTE
author: windows-driver-content
description: The DecodeExtensionExecute function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) nonstandard decode device.
old-location: display\decodeextensionexecute.htm
old-project: display
ms.assetid: 522a552a-4588-4dd1-b81f-73ccd4a1c0aa
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DecodeExtensionExecute
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_DECODEEXTENSIONEXECUTE callback



## -description
<p>The <b>DecodeExtensionExecute</b> function performs a decode operation by using the given Microsoft DirectX Video Accelerator (VA) nonstandard decode device.</p>


## -prototype

````
PFND3DDDI_DECODEEXTENSIONEXECUTE DecodeExtensionExecute;

__checkReturn HRESULT APIENTRY DecodeExtensionExecute(
  _In_          HANDLE                           hDevice,
  _Inout_ const D3DDDIARG_DECODEEXTENSIONEXECUTE *pData
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param pData [in, out]

<dd>
<p> A pointer to a <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodeextensionexecute.md">D3DDDIARG_DECODEEXTENSIONEXECUTE</a> structure that describes the DirectX VA decode operation to perform.</p>
</dd>
</dl>

## -returns
<p><b>DecodeExtensionExecute</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The DirectX VA decode operation is successfully performed.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-decodeextensionexecute.md">DecodeExtensionExecute</a> could not allocate the required memory for it to complete.</p>

<p> </p>

## -remarks
<p>A user-mode display driver can implement the <b>DecodeExtensionExecute</b> function to support extensions to the standard decode types (that is, nonstandard decode GUIDs). These nonstandard decode types are useful for configuring encryption and other miscellaneous enhancements. </p>

<p><b>DecodeExtensionExecute</b> is called when DirectX VA 2.0 decoders require the nonstandard extensions.</p>

<p>For compatibility with DirectX VA 1.0 decoders that might require these nonstandard extensions, <b>DecodeExtensionExecute</b> is called whenever a DirectX VA 1.0 decoder makes an execution call in which any bDXVA_Func value that is greater than 4 is set in the most significant 8 bits of the <b>Function</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodeextensionexecute.md">D3DDDIARG_DECODEEXTENSIONEXECUTE</a> structure. <b>DecodeExtensionExecute</b> is also called whenever DirectX VA 1.0 decoder makes a configuration call in which any DXVA_ConfigQueryOrReplyFunc flag other than DXVA_QUERYORREPLYFUNCFLAG_DECODER_PROBE_QUERY (0xFFFFF1) or DXVA_QUERYORREPLYFUNCFLAG_DECODER_LOCK_QUERY (0xFFFFF5) flag is set in the most significant 24 bits of <b>Function</b>. For more information about the meanings for the bit settings of <b>Function</b>, see the <a href="https://msdn.microsoft.com/bfb1a98e-b9f0-4baa-b486-b2ff33a8bac5">DXVA_ConfigQueryOrReplyFlag and DXVA_ConfigQueryorReplyFunc Variables</a> and <a href="https://msdn.microsoft.com/6db9fa71-7bc2-4eb6-afcb-b16df48f7e8b">bDXVA_Func Variable</a> topics. </p>

<p>Because of compatibility issues with DirectX VA 1.0 decoders that might make such a configuration call before DXVA_QUERYORREPLYFUNCFLAG_DECODER_LOCK_QUERY, those decoders can make such a configuration call also before a decode device is created. If such a configuration call is made before a decode device is created, the <b>hDecode</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodeextensionexecute.md">D3DDDIARG_DECODEEXTENSIONEXECUTE</a> structure that the <i>pData</i> parameter points to is set to <b>NULL</b>. In this situation, the driver might be required to return an error (for example, E_FAIL) if the driver cannot support the situation independent of a decode device. </p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-decodeextensionexecute.md">D3DDDIARG_DECODEEXTENSIONEXECUTE</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--d3dddi-devicefuncs.md">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DECODEEXTENSIONEXECUTE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
