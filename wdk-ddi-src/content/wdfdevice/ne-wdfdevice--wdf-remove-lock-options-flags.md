---
UID: NE.wdfdevice._WDF_REMOVE_LOCK_OPTIONS_FLAGS
title: WDF_REMOVE_LOCK_OPTIONS_FLAGS
author: windows-driver-content
description: The WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REMOVE_LOCK_OPTIONS structure.
old-location: wdf\wdf_remove_lock_options_flags.htm
old-project: wdf
ms.assetid: 3822B8A2-1EFB-45C7-A7DB-FBCE76A06336
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_REMOVE_LOCK_OPTIONS_FLAGS
req.alt-loc: wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_REMOVE_LOCK_OPTIONS_FLAGS</b> enumeration type defines flags that are used in a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh406495">WDF_REMOVE_LOCK_OPTIONS</a> structure.</p>


## -syntax

````
typedef enum _WDF_REMOVE_LOCK_OPTIONS_FLAGS { 
  WDF_REMOVE_LOCK_OPTION_ACQUIRE_FOR_IO  = 1
} WDF_REMOVE_LOCK_OPTIONS_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDF_REMOVE_LOCK_OPTION_ACQUIRE_FOR_IO"></a><a id="wdf_remove_lock_option_acquire_for_io"></a><b>WDF_REMOVE_LOCK_OPTION_ACQUIRE_FOR_IO</b>

<dd>
<p>Specifies that the framework should acquire a remove lock before delivering an IRP of any type to the driver.</p>
</dd>
</dl>

## -remarks
<p>For more information about using remove locks in a framework-based driver, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451095">WdfDeviceInitSetRemoveLockOptions</a>.</p>

<p>For more information about using remove locks in a framework-based driver, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451095">WdfDeviceInitSetRemoveLockOptions</a>.</p>

<p>For more information about using remove locks in a framework-based driver, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh451095">WdfDeviceInitSetRemoveLockOptions</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451095">WdfDeviceInitSetRemoveLockOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406501">WDF_REMOVE_LOCK_OPTIONS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406495">WDF_REMOVE_LOCK_OPTIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
