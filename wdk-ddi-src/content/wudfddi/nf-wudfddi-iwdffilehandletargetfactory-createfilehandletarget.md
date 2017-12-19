---
UID: NF.wudfddi.IWDFFileHandleTargetFactory.CreateFileHandleTarget
title: IWDFFileHandleTargetFactory::CreateFileHandleTarget method
author: windows-driver-content
description: The CreateFileHandleTarget method creates a file-handle-based I/O target object.
old-location: wdf\iwdffilehandletargetfactory_createfilehandletarget.htm
old-project: wdf
ms.assetid: 579a2cef-1e37-426c-9f69-8766dc9011ba
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFFileHandleTargetFactory, IWDFFileHandleTargetFactory::CreateFileHandleTarget, CreateFileHandleTarget
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFFileHandleTargetFactory::CreateFileHandleTarget method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>CreateFileHandleTarget</b> method creates a file-handle-based I/O target object.



## -syntax

````
HRESULT CreateFileHandleTarget(
  [in]  HANDLE       hTarget,
  [out] IWDFIoTarget **ppTarget
);
````


## -parameters

### -param hTarget [in]

A handle to the target device. The handle must have been previously opened with the FILE_FLAG_OVERLAPPED flag. For example, FILE_FLAG_OVERLAPPED must have been specified in the <i>dwFlagsAndAttributes</i> parameter of the Microsoft Win32 <b>CreateFile</b> function. 


### -param ppTarget [out]

A pointer to a location that receives a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a> interface of the I/O target object.


## -returns
<b>CreateFileHandleTarget</b> returns one of the following values: 
<dl>
<dt><b>S_OK </b></dt>
</dl>
<a href="wdf.iwdffilehandletargetfactory_createfilehandletarget">CreateFileHandleTarget</a> successfully created a file-handle-based I/O target object. 
<dl>
<dt><b>E_OUTOFMEMORY </b></dt>
</dl>
<a href="wdf.iwdffilehandletargetfactory_createfilehandletarget">CreateFileHandleTarget</a> encountered an allocation failure.

 

<b>CreateFileHandleTarget</b> might also return other HRESULT values that are defined in Winerror.h.




## -remarks
If your driver uses a file-handle-based I/O target, the <b>DDInstall.WDF</b> section of the driver's INF file must set the <b>UmdfDispatcher</b> directive to <b>FileHandle</b>. For more information about <b>UmdfDispatcher</b>, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives</a>.

After the driver creates a file-handle-based I/O target object, it can format I/O requests and send them to the I/O target. Typically, if the driver calls <a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a>, <a href="wdf.iwdfiotarget_formatrequestforwrite">IWDFIoTarget::FormatRequestForWrite</a>, or <a href="wdf.iwdfiotarget_formatrequestforioctl">IWDFIoTarget::FormatRequestForIoctl</a>, the driver sets the <i>pFile</i> parameter to <b>NULL</b>. The <b>NULL</b> causes the framework to use the filename that the driver specified to <b>CreateFileHandleTarget</b>. If the driver provides a non-<b>NULL</b> <i>pFile</i> parameter, the specified file replaces the file that the driver specified to <b>CreateFileHandleTarget</b>. (Drivers can also call <a href="wdf.iwdfiorequest_formatusingcurrenttype">IWDFIoRequest::FormatUsingCurrentType</a> to format an I/O request.)

When the driver calls <a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a> to send the I/O request to the I/O target, the driver must not set the <a href="wdf.wdf_request_send_options_flags__umdf_">WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</a> value in the <i>Flags</i> parameter. 

The Win32 handle that the driver passes to <b>CreateFileHandleTarget</b> must remain valid for the lifetime of the file-handle-based I/O target object. (The framework does not take a reference on this target handle, so your driver must ensure that the Win32 handle remains valid.)

When the driver has finished using the <a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a> interface that <b>CreateFileHandleTarget</b> provides, it must release the <b>IWDFIoTarget</b> interface.

For more information about <b>CreateFileHandleTarget</b> and I/O targets, see <a href="wdf.initializing_a_general_i_o_target_in_umdf">Initializing a General I/O Target in UMDF</a>.

The following code example shows how to create a file-handle-based I/O target for a named pipe. In this example, <i>m_FxDevice</i> is the interface pointer that <a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a> provides.


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
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfusb.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdffilehandletargetfactory.md">IWDFFileHandleTargetFactory</a>
</dt>
<dt>
<a href="wdf.iwdfiorequest_send">IWDFIoRequest::Send</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfiotarget.md">IWDFIoTarget</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFFileHandleTargetFactory::CreateFileHandleTarget method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

