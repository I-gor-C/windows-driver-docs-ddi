---
UID: NF.wudfddi.IWDFDevice.CreateRequest
title: IWDFDevice::CreateRequest
author: windows-driver-content
description: The CreateRequest method creates an unformatted request object.
old-location: wdf\iwdfdevice_createrequest.htm
old-project: wdf
ms.assetid: 031ce604-9d6f-4fdd-bacc-d1897f260a14
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFDevice, CreateRequest, IWDFDevice::CreateRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDevice.CreateRequest
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
req.iface: IWDFDevice
req.product: Windows 10 or later.
---

# IWDFDevice::CreateRequest method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateRequest</b> method creates an unformatted request object.</p>


## -syntax

````
HRESULT CreateRequest(
  [in, optional] IUnknown      *pCallbackInterface,
  [in, optional] IWDFObject    *pParentObject,
  [out]          IWDFIoRequest **ppRequest
);
````


## -parameters
<dl>

### -param <i>pCallbackInterface</i> [in, optional]

<dd>
<p>A pointer to the <b>IUnknown</b> interface that the framework uses to determine the object-related event callback functions that the driver subscribes to on the newly created request object. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require notification. If the driver passes a valid pointer, the framework will call <b>QueryInterface</b> on the <b>IUnknown</b> interface for the <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface. If the framework obtains the driver's <b>IObjectCleanup</b> interface, the framework can subsequently call the driver's <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> method to notify the driver that the request object is cleaned up. </p>
</dd>

### -param <i>pParentObject</i> [in, optional]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a> interface for the parent object of the created I/O request object. If <b>NULL</b>, the device object becomes the default parent. </p>
</dd>

### -param <i>ppRequest</i> [out]

<dd>
<p>A pointer to a variable that receives a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a> interface for the new request object.</p>
</dd>
</dl>

## -returns
<p><b>CreateRequest</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Before a UMDF driver uses the request object that <b>CreateRequest</b> creates, the driver must format the request object. To format an I/O request object, the driver calls one of the following methods:</p>

<p>
<a href="wdf.iwdfiotarget_formatrequestforioctl">IWDFIoTarget::FormatRequestForIoctl</a>
</p>

<p>
<a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a>
</p>

<p>
<a href="wdf.iwdfiotarget_formatrequestforwrite">IWDFIoTarget::FormatRequestForWrite</a>
</p>

<p>If a driver calls <b>CreateRequest</b> to create a request object, it must not call <a href="wdf.iwdfiorequest_complete">IWDFIoRequest::Complete</a> for the request object. Instead, the driver must call <a href="wdf.iwdfobject_deletewdfobject">IWDFObject::DeleteWdfObject</a> when it has finished using the request object. For more information, see <a href="wdf.completing_i_o_requests">Completing I/O Requests</a>.</p>

<p>If <b>NULL</b> is specified in the <i>pParentObject</i> parameter, the device object becomes the default parent object for the newly created I/O request object. If a UMDF driver creates an I/O request object that the driver uses with a specific I/O queue object or another I/O request object, the driver should set that queue or request object as the created request object's parent object. When the parent object is deleted, the created request object is deleted. </p>

<p>The following code example shows how to create a request, format the request for reading, and send the request on.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfdevice.md">IWDFDevice</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfiorequest.md">IWDFIoRequest</a>
</dt>
<dt>
<a href="wdf.iwdfiotarget_formatrequestforioctl">IWDFIoTarget::FormatRequestForIoctl</a>
</dt>
<dt>
<a href="wdf.iwdfiotarget_formatrequestforread">IWDFIoTarget::FormatRequestForRead</a>
</dt>
<dt>
<a href="wdf.iwdfiotarget_formatrequestforwrite">IWDFIoTarget::FormatRequestForWrite</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice::CreateRequest method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
