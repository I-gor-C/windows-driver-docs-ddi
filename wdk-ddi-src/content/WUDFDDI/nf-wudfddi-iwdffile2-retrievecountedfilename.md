---
UID: NF.wudfddi.IWDFFile2.RetrieveCountedFileName
title: IWDFFile2::RetrieveCountedFileName
author: windows-driver-content
description: The RetrieveCountedFileName method retrieves the full counted file name for a file that is associated with a device.
old-location: wdf\iwdffile2_retrievecountedfilename.htm
ms.assetid: 0b3aa8d9-1947-4e5e-91d1-6f73ddb3908a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFFile2.RetrieveCountedFileName
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: IWDFFile2, RetrieveCountedFileName, IWDFFile2::RetrieveCountedFileName
req.iface: IWDFFile2
req.product: Windows 10 or later.
---

# IWDFFile2::RetrieveCountedFileName method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>RetrieveCountedFileName</b> method retrieves the full counted file name for a file that is associated with a device. </p>


## -syntax

````
HRESULT RetrieveCountedFileName(
  [out]     WCHAR *pCountedFileName,
  [in, out] DWORD *pdwCountedFileNameLength
);
````


## -parameters
<dl>

### -param <i>pCountedFileName</i> [out]

<dd>
<p>A pointer to a caller-allocated buffer. This buffer receives a <b>NULL</b>-terminated character string that represents the full name of the file that is associated with the device. If the pointer is <b>NULL</b>, <b>RetrieveCountedFileName</b> retrieves only the string length. </p>
</dd>

### -param <i>pdwCountedFileNameLength</i> [in, out]

<dd>
<p>A pointer to a caller-allocated variable. On input, the driver sets the variable to the length, in characters, of the buffer that <i>pdwFileNameLengthInChars</i> points to. On output, the framework sets the variable to the length, in characters, of the character string (including the terminating <b>NULL</b> character) that it placed in the buffer. If a counted file name does not exist, the framework sets the variable to zero. </p>
</dd>
</dl>

## -returns
<p><b>RetrieveCountedFileName</b> returns S_OK if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>E_POINTER</b></dt>
</dl><p>The <i>pdwCountedFileNameLength</i> pointer is <b>NULL</b>.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_INVALID_PARAMETER)</b></dt>
</dl><p>The counted file name is invalid.</p><dl>
<dt><b>E_NOT_SUFFICIENT_BUFFER</b></dt>
</dl><p>The buffer that <i>pCountedFileName</i> points to is too small.</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains.</p>

## -remarks
<p>A counted file name is a string that can include embedded <b>NULL</b> ('\0') characters in addition to a terminating <b>NULL</b>. To obtain a name string without embedded <b>NULL</b> characters, drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff558939">IWDFFile::RetrieveFileName</a>.</p>

<p>Typically, a driver calls <b>RetrieveCountedFileName</b> twice, using the following steps:</p>

<p>The driver calls <b>RetrieveCountedFileName</b> with the <i>pCountedFileName</i> parameter set to <b>NULL</b>, to obtain the required buffer length.</p>

<p>The driver allocates a buffer of the required size.</p>

<p>The driver calls <b>RetrieveCountedFileName</b> again to obtain the file name string.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558915">IWDFFile2</a> interface from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface that a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556841">IQueueCallbackCreate::OnCreateFile</a> callback function receives. The example calls <b>RetrieveCountedFileName</b> twice--once to obtain the file name's length and once to retrieve the file name string.</p>

<p>A counted file name is a string that can include embedded <b>NULL</b> ('\0') characters in addition to a terminating <b>NULL</b>. To obtain a name string without embedded <b>NULL</b> characters, drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff558939">IWDFFile::RetrieveFileName</a>.</p>

<p>Typically, a driver calls <b>RetrieveCountedFileName</b> twice, using the following steps:</p>

<p>The driver calls <b>RetrieveCountedFileName</b> with the <i>pCountedFileName</i> parameter set to <b>NULL</b>, to obtain the required buffer length.</p>

<p>The driver allocates a buffer of the required size.</p>

<p>The driver calls <b>RetrieveCountedFileName</b> again to obtain the file name string.</p>

<p>The following code example obtains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558915">IWDFFile2</a> interface from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface that a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556841">IQueueCallbackCreate::OnCreateFile</a> callback function receives. The example calls <b>RetrieveCountedFileName</b> twice--once to obtain the file name's length and once to retrieve the file name string.</p>

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
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558915">IWDFFile2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558939">IWDFFile::RetrieveFileName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFFile2::RetrieveCountedFileName method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
