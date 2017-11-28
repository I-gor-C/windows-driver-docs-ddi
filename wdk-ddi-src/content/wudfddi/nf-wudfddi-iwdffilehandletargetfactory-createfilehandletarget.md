---
UID: NF.wudfddi.IWDFFileHandleTargetFactory.CreateFileHandleTarget
title: IWDFFileHandleTargetFactory::CreateFileHandleTarget
author: windows-driver-content
description: The CreateFileHandleTarget method creates a file-handle-based I/O target object.
old-location: wdf\iwdffilehandletargetfactory_createfilehandletarget.htm
old-project: wdf
ms.assetid: 579a2cef-1e37-426c-9f69-8766dc9011ba
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFFileHandleTargetFactory, CreateFileHandleTarget, IWDFFileHandleTargetFactory::CreateFileHandleTarget
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfusb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFFileHandleTargetFactory.CreateFileHandleTarget
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
req.iface: IWDFFileHandleTargetFactory
req.product: Windows 10 or later.
---

# IWDFFileHandleTargetFactory::CreateFileHandleTarget method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateFileHandleTarget</b> method creates a file-handle-based I/O target object.</p>


## -syntax

````
HRESULT CreateFileHandleTarget(
  [in]  HANDLE       hTarget,
  [out] IWDFIoTarget **ppTarget
);
````


## -parameters
<dl>

### -param <i>hTarget</i> [in]

<dd>
<p>A handle to the target device. The handle must have been previously opened with the FILE_FLAG_OVERLAPPED flag. For example, FILE_FLAG_OVERLAPPED must have been specified in the <i>dwFlagsAndAttributes</i> parameter of the Microsoft Win32 <b>CreateFile</b> function. </p>
</dd>

### -param <i>ppTarget</i> [out]

<dd>
<p>A pointer to a location that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a> interface of the I/O target object.</p>
</dd>
</dl>

## -returns
<p><b>CreateFileHandleTarget</b> returns one of the following values: </p><dl>
<dt><b>S_OK </b></dt>
</dl><p>
<a href="wdf.iwdffilehandletargetfactory_createfilehandletarget">CreateFileHandleTarget</a> successfully created a file-handle-based I/O target object. </p><dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl><p>
<a href="wdf.iwdffilehandletargetfactory_createfilehandletarget">CreateFileHandleTarget</a> encountered an allocation failure.</p>

<p> </p>

<p><b>CreateFileHandleTarget</b> might also return other HRESULT values that are defined in Winerror.h.

</p>

## -remarks
<p>If your driver uses a file-handle-based I/O target, the <b>DDInstall.WDF</b> section of the driver's INF file must set the <b>UmdfDispatcher</b> directive to <b>FileHandle</b>. For more information about <b>UmdfDispatcher</b>, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives</a>.</p>

<p>After the driver creates a file-handle-based I/O target object, it can format I/O requests and send them to the I/O target. Typically, if the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559233">IWDFIoTarget::FormatRequestForRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559236">IWDFIoTarget::FormatRequestForWrite</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559230">IWDFIoTarget::FormatRequestForIoctl</a>, the driver sets the <i>pFile</i> parameter to <b>NULL</b>. The <b>NULL</b> causes the framework to use the filename that the driver specified to <b>CreateFileHandleTarget</b>. If the driver provides a non-<b>NULL</b> <i>pFile</i> parameter, the specified file replaces the file that the driver specified to <b>CreateFileHandleTarget</b>. (Drivers can also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559077">IWDFIoRequest::FormatUsingCurrentType</a> to format an I/O request.)</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a> to send the I/O request to the I/O target, the driver must not set the <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-send-options-flags.md">WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</a> value in the <i>Flags</i> parameter. </p>

<p>The Win32 handle that the driver passes to <b>CreateFileHandleTarget</b> must remain valid for the lifetime of the file-handle-based I/O target object. (The framework does not take a reference on this target handle, so your driver must ensure that the Win32 handle remains valid.)</p>

<p>When the driver has finished using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a> interface that <b>CreateFileHandleTarget</b> provides, it must release the <b>IWDFIoTarget</b> interface.</p>

<p>For more information about <b>CreateFileHandleTarget</b> and I/O targets, see <a href="wdf.initializing_a_general_i_o_target_in_umdf">Initializing a General I/O Target in UMDF</a>.</p>

<p>The following code example shows how to create a file-handle-based I/O target for a named pipe. In this example, <i>m_FxDevice</i> is the interface pointer that <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> provides.</p>

<p>If your driver uses a file-handle-based I/O target, the <b>DDInstall.WDF</b> section of the driver's INF file must set the <b>UmdfDispatcher</b> directive to <b>FileHandle</b>. For more information about <b>UmdfDispatcher</b>, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives</a>.</p>

<p>After the driver creates a file-handle-based I/O target object, it can format I/O requests and send them to the I/O target. Typically, if the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559233">IWDFIoTarget::FormatRequestForRead</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff559236">IWDFIoTarget::FormatRequestForWrite</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff559230">IWDFIoTarget::FormatRequestForIoctl</a>, the driver sets the <i>pFile</i> parameter to <b>NULL</b>. The <b>NULL</b> causes the framework to use the filename that the driver specified to <b>CreateFileHandleTarget</b>. If the driver provides a non-<b>NULL</b> <i>pFile</i> parameter, the specified file replaces the file that the driver specified to <b>CreateFileHandleTarget</b>. (Drivers can also call <a href="https://msdn.microsoft.com/library/windows/hardware/ff559077">IWDFIoRequest::FormatUsingCurrentType</a> to format an I/O request.)</p>

<p>When the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a> to send the I/O request to the I/O target, the driver must not set the <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-send-options-flags.md">WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</a> value in the <i>Flags</i> parameter. </p>

<p>The Win32 handle that the driver passes to <b>CreateFileHandleTarget</b> must remain valid for the lifetime of the file-handle-based I/O target object. (The framework does not take a reference on this target handle, so your driver must ensure that the Win32 handle remains valid.)</p>

<p>When the driver has finished using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a> interface that <b>CreateFileHandleTarget</b> provides, it must release the <b>IWDFIoTarget</b> interface.</p>

<p>For more information about <b>CreateFileHandleTarget</b> and I/O targets, see <a href="wdf.initializing_a_general_i_o_target_in_umdf">Initializing a General I/O Target in UMDF</a>.</p>

<p>The following code example shows how to create a file-handle-based I/O target for a named pipe. In this example, <i>m_FxDevice</i> is the interface pointer that <a href="https://msdn.microsoft.com/library/windows/hardware/ff558899">IWDFDriver::CreateDevice</a> provides.</p>

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
<dt>Wudfddi.h (include Wudfusb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558926">IWDFFileHandleTargetFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559149">IWDFIoRequest::Send</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559170">IWDFIoTarget</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFFileHandleTargetFactory::CreateFileHandleTarget method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
