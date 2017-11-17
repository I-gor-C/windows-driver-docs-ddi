---
UID: NF.bidispl.IBidiRequest.SetInputData
title: IBidiRequest::SetInputData
author: windows-driver-content
description: The IBidiRequest::SetInputData method sets the data to send to the printer.
old-location: print\ibidirequest_ibidirequest__setinputdata.htm
ms.assetid: 8db7b5cd-b03f-4973-8711-8ac022bfb2b5
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: bidispl.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IBidiRequest.IBidiRequest::SetInputData
req.alt-loc: bidispl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Bidispl.dll
req.irql: PASSIVE_LEVEL
ms.keywords: IBidiRequest, SetInputData, IBidiRequest::SetInputData
req.iface: IBidiRequest
---

# IBidiRequest::SetInputData method



## -description
<p>The <b>IBidiRequest::SetInputData</b> method sets the data to send to the printer.</p>


## -syntax

````
HRESULT IBidiRequest::SetInputData(
  [in] const DWORD dwType,
  [in] const BYTE  *pData,
  [in] const UINT  uSize
);
````


## -parameters
<dl>

### -param <i>dwType</i> [in]

<dd>
<p>The type of data to be sent. This parameter can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="BIDI_NULL"></a><a id="bidi_null"></a><dl>

### -param <b>BIDI_NULL</b>

</dl>
</td>
<td width="60%">
<p>No data.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_INT"></a><a id="bidi_int"></a><dl>

### -param <b>BIDI_INT</b>

</dl>
</td>
<td width="60%">
<p>Integer data.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_FLOAT"></a><a id="bidi_float"></a><dl>

### -param <b>BIDI_FLOAT</b>

</dl>
</td>
<td width="60%">
<p>Floating-point number.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_BOOL"></a><a id="bidi_bool"></a><dl>

### -param <b>BIDI_BOOL</b>

</dl>
</td>
<td width="60%">
<p><b>TRUE</b> or <b>FALSE</b>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_STRING"></a><a id="bidi_string"></a><dl>

### -param <b>BIDI_STRING</b>

</dl>
</td>
<td width="60%">
<p>Unicode character string.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_TEXT"></a><a id="bidi_text"></a><dl>

### -param <b>BIDI_TEXT</b>

</dl>
</td>
<td width="60%">
<p>Non-localizable Unicode string.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_ENUM"></a><a id="bidi_enum"></a><dl>

### -param <b>BIDI_ENUM</b>

</dl>
</td>
<td width="60%">
<p>Enumeration data in the form of a Unicode string.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BIDI_BLOB"></a><a id="bidi_blob"></a><dl>

### -param <b>BIDI_BLOB</b>

</dl>
</td>
<td width="60%">
<p>Binary data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to the byte array that contains the data. For example, if <i>dwType</i> is BIDI_BOOL, <i>pData</i> points to a buffer that contains a Boolean value and if <i>dwType</i> is BIDI_BLOB, <i>pData</i> points to a buffer that contains the binary data.</p>
</dd>

### -param <i>uSize</i> [in]

<dd>
<p>Size, in bytes, of the byte array specified by <i>pData</i>.</p>
</dd>
</dl>

## -returns
<p>The method returns one of the following values. For more information about COM error codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544310">Error Handling</a>.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successfully carried out.</p><dl>
<dt><b>E_HANDLE</b></dt>
</dl><p>The interface handle was invalid.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The type of the data was not consistent with its size.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>Memory allocation failed.</p><dl>
<dt><b>None of the above</b></dt>
</dl><p>The <b>HRESULT</b> contains an error code corresponding to the last error.</p>

<p> </p>

## -remarks
<p>If an application calls <b>SetInputData</b> more than once, only the value of the last call will be set.</p>

<p>If an application calls <b>SetInputData</b> more than once, only the value of the last call will be set.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows XP</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2003</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bidispl.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Bidispl.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>
</dt>
<dt>
<a href="NULL">Bidirectional Communication Schema</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dd144969">IBidiRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiRequest::IBidiRequest::SetInputData method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
