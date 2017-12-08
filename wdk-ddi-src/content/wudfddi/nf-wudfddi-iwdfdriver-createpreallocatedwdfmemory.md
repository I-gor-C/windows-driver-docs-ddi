---
UID: NF.wudfddi.IWDFDriver.CreatePreallocatedWdfMemory
title: IWDFDriver::CreatePreallocatedWdfMemory
author: windows-driver-content
description: The CreatePreallocatedWdfMemory method creates a framework memory object for the specified buffer.
old-location: wdf\iwdfdriver_createpreallocatedwdfmemory.htm
old-project: wdf
ms.assetid: 9c24f42b-0f1d-4b93-99af-f4a5069b5223
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDriver, CreatePreallocatedWdfMemory, IWDFDriver::CreatePreallocatedWdfMemory
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
req.alt-api: IWDFDriver.CreatePreallocatedWdfMemory
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

# IWDFDriver::CreatePreallocatedWdfMemory method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreatePreallocatedWdfMemory</b> method creates a <a href="wdf.framework_memory_object">framework memory object</a> for the specified buffer.</p>


## -syntax

````
HRESULT CreatePreallocatedWdfMemory(
  [in]           BYTE       *pBuff,
  [in]           SIZE_T     BufferSize,
  [in, optional] IUnknown   *pCallbackInterface,
  [in, optional] IWDFObject *pParentObject,
  [out]          IWDFMemory **ppWdfMemory
);
````


## -parameters
<dl>

### -param pBuff [in]

<dd>
<p>A pointer to a driver-supplied data buffer for the memory object.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>
      The size, in bytes, of data that <i>pBuff</i> points to.
     </p>
</dd>

### -param pCallbackInterface [in, optional]

<dd>
<p>A pointer to the <b>IUnknown</b> interface that the framework uses to determine the object-related event callback functions that the driver subscribes to on the newly created memory object. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require notification. The <b>IUnknown</b> interface is used for object cleanup and disposal. If the driver passes a valid pointer, the framework will call <b>QueryInterface</b> on the <b>IUnknown</b> interface for the <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface. If the framework obtains the driver's <b>IObjectCleanup</b> interface, the framework can subsequently call the driver's <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> method to notify the driver that the memory object is cleaned up. </p>
</dd>

### -param pParentObject [in, optional]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a> interface for the parent object of the created memory object. If <b>NULL</b>, the driver object becomes the default parent. </p>
</dd>

### -param ppWdfMemory [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a> interface for the newly created WDF memory object.</p>
</dd>
</dl>

## -returns
<p><b>CreatePreallocatedWdfMemory</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The <b>CreatePreallocatedWdfMemory</b> method creates a framework memory object for a buffer that the driver previously allocated or obtained. </p>

<p>A UMDF driver can call <b>CreatePreallocatedWdfMemory</b> if it must create a memory object that represents a pre-existing memory buffer. For example, the driver might receive a driver-defined structure within a buffer for an I/O request that contains an internal I/O control code. The driver can call <b>CreatePreallocatedWdfMemory</b> to create a memory object so that the driver can pass the structure to an I/O target. </p>

<p>After a UMDF driver calls <b>CreatePreallocatedWdfMemory</b>, the driver can call <a href="wdf.iwdfmemory_setbuffer">IWDFMemory::SetBuffer</a> to assign a different buffer to the memory object that <b>CreatePreallocatedWdfMemory</b> created. </p>

<p>When the framework memory object that <b>CreatePreallocatedWdfMemory</b> created is deleted, the framework does not deallocate the pre-existing buffer. Likewise, a call to <a href="wdf.iwdfmemory_setbuffer">IWDFMemory::SetBuffer</a> does not deallocate the previously assigned buffer.</p>

<p>The following code example shows how to create a memory object for a buffer.</p>

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
<a href="..\wudfddi\nn-wudfddi-iwdfdriver.md">IWDFDriver</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a>
</dt>
<dt>
<a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a>
</dt>
<dt>
<a href="wdf.iwdfmemory_setbuffer">IWDFMemory::SetBuffer</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDriver::CreatePreallocatedWdfMemory method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
