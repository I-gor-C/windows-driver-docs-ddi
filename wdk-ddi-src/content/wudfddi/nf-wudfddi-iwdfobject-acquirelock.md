---
UID: NF.wudfddi.IWDFObject.AcquireLock
title: IWDFObject::AcquireLock method
author: windows-driver-content
description: The AcquireLock method prevents the framework from calling methods of interfaces that a driver registered.
old-location: wdf\iwdfobject_acquirelock.htm
old-project: wdf
ms.assetid: f69328fb-356b-4381-ae6e-df39ac60e032
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFObject, IWDFObject::AcquireLock, AcquireLock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFObject.AcquireLock
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

# IWDFObject::AcquireLock method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>AcquireLock</b> method prevents the framework from calling methods of interfaces that a driver registered.



## -syntax

````
void AcquireLock();
````


## -parameters


## -returns
None

None

None


## -remarks
If a driver configured itself to use the <b>AcquireLock</b> locking scheme, the framework automatically acquires the "presentation" lock before calling into the driver. (For more information about this locking scheme, see <a href="wdf.specifying_a_callback_synchronization_mode">Specifying a Callback Synchronization Mode</a>.) The <b>AcquireLock</b> and <a href="wdf.iwdfobject_releaselock">IWDFObject::ReleaseLock</a> methods acquire and release the presentation lock, respectively. <a href="wdf.framework_device_object">Framework device objects</a> and <a href="wdf.framework_i_o_queue_object">framework I/O queue objects</a> currently support the <b>AcquireLock</b> method.

The driver calls the <b>AcquireLock</b> method to manipulate its objects that were created from its callback interfaces outside the callback scope in a thread-safe manner. The <b>AcquireLock</b> method represents an advanced feature of the framework that most drivers will not use because improper usage can result in deadlocks.

Unsynchronized code can call <b>AcquireLock</b>. The driver should call on objects that match its synchronization scope.

For a code example of how to use the <b>AcquireLock</b> method, see <a href="wdf.iwdfdevice_setpnpstate">IWDFDevice::SetPnpState</a>.


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
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>
</dt>
<dt>
<a href="wdf.iwdfobject_releaselock">IWDFObject::ReleaseLock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFObject::AcquireLock method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

