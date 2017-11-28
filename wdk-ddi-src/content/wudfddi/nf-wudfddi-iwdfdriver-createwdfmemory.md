---
UID: NF.wudfddi.IWDFDriver.CreateWdfMemory
title: IWDFDriver::CreateWdfMemory
author: windows-driver-content
description: The CreateWdfMemory method creates a framework memory object and allocates, for the memory object, a data buffer of the specified nonzero size.
old-location: wdf\iwdfdriver_createwdfmemory.htm
old-project: wdf
ms.assetid: 2ea754db-3bed-48d9-825f-7ee7b5e169b7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDriver, CreateWdfMemory, IWDFDriver::CreateWdfMemory
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
req.alt-api: IWDFDriver.CreateWdfMemory
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
req.iface: IWDFDriver
req.product: Windows 10 or later.
---

# IWDFDriver::CreateWdfMemory method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateWdfMemory</b> method creates a <a href="wdf.framework_memory_object">framework memory object</a> and allocates, for the memory object, a data buffer of the specified nonzero size.</p>


## -syntax

````
HRESULT CreateWdfMemory(
  [in]           SIZE_T     BufferSize,
  [in, optional] IUnknown   *pCallbackInterface,
  [in, optional] IWDFObject *pParentObject,
  [out]          IWDFMemory **ppWdfMemory
);
````


## -parameters
<dl>

### -param <i>BufferSize</i> [in]

<dd>
<p>
            The nonzero specified size, in bytes, of data for the newly created WDF memory object's data buffer. 
          </p>
</dd>

### -param <i>pCallbackInterface</i> [in, optional]

<dd>
<p>A pointer to the <b>IUnknown</b> interface that the framework uses to determine the object-related event callback functions that the driver subscribes to on the newly created memory object. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require notification. The <b>IUnknown</b> interface is used for object cleanup and disposal. If the driver passes a valid pointer, the framework will call <b>QueryInterface</b> on the <b>IUnknown</b> interface for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a> interface. If the framework obtains the driver's <b>IObjectCleanup</b> interface, the framework can subsequently call the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556760">IObjectCleanup::OnCleanup</a> method to notify the driver that the memory object is cleaned up. </p>
</dd>

### -param <i>pParentObject</i> [in, optional]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a> interface for the parent object of the created memory object. If <b>NULL</b>, the driver object becomes the default parent. </p>
</dd>

### -param <i>ppWdfMemory</i> [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface for the newly created WDF memory object.</p>
</dd>
</dl>

## -returns
<p><b>CreateWdfMemory</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The <b>CreateWdfMemory</b> method allocates a buffer of the size that the <i>BufferSize</i> parameter specifies, and creates a framework memory object that represents the buffer. </p>

<p>If <b>NULL</b> is specified in the <i>pParentObject</i> parameter, the driver object becomes the default parent object for the newly created memory object. If a UMDF driver creates a memory object that the driver uses with a specific device object, request object, or other framework object, the driver should set the memory object's parent object appropriately. When the parent object is deleted, the memory object and its buffer are deleted. </p>

<p>A UMDF driver can also delete a memory object and its buffer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a>. </p>

<p>A UMDF driver cannot create a memory object with a zero-specified size buffer. If a driver must use a zero-specified size buffer, the driver should use a <b>NULL</b> memory object instead. For example, if the driver must use a zero-specified size buffer in a read request, the driver must pass <b>NULL</b> to the <i>pOutputMemory</i> parameter in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559233">IWDFIoTarget::FormatRequestForRead</a> method.</p>

<p>The following code example shows how to create a memory object that can hold information that is read from a USB endpoint.</p>

<p>The <b>CreateWdfMemory</b> method allocates a buffer of the size that the <i>BufferSize</i> parameter specifies, and creates a framework memory object that represents the buffer. </p>

<p>If <b>NULL</b> is specified in the <i>pParentObject</i> parameter, the driver object becomes the default parent object for the newly created memory object. If a UMDF driver creates a memory object that the driver uses with a specific device object, request object, or other framework object, the driver should set the memory object's parent object appropriately. When the parent object is deleted, the memory object and its buffer are deleted. </p>

<p>A UMDF driver can also delete a memory object and its buffer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a>. </p>

<p>A UMDF driver cannot create a memory object with a zero-specified size buffer. If a driver must use a zero-specified size buffer, the driver should use a <b>NULL</b> memory object instead. For example, if the driver must use a zero-specified size buffer in a read request, the driver must pass <b>NULL</b> to the <i>pOutputMemory</i> parameter in a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559233">IWDFIoTarget::FormatRequestForRead</a> method.</p>

<p>The following code example shows how to create a memory object that can hold information that is read from a USB endpoint.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558893">IWDFDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556754">IObjectCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556760">IObjectCleanup::OnCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559233">IWDFIoTarget::FormatRequestForRead</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDriver::CreateWdfMemory method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
