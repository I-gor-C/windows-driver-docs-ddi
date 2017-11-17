---
UID: NF.wdfwmi.WdfWmiInstanceFireEvent
title: WdfWmiInstanceFireEvent
author: windows-driver-content
description: The WdfWmiInstanceFireEvent method sends a WMI event to WMI clients that have registered to receive event notification.
old-location: wdf\wdfwmiinstancefireevent.htm
ms.assetid: 7bef79ab-78d6-47b6-a3f4-d9733ffcb53d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWmiInstanceFireEvent
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: WdfWmiInstanceFireEvent
req.iface: 
req.product: Windows 10 or later.
---

# WdfWmiInstanceFireEvent function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfWmiInstanceFireEvent</b> method sends a WMI event to WMI clients that have registered to receive event notification.</p>


## -syntax

````
NTSTATUS WdfWmiInstanceFireEvent(
  _In_     WDFWMIINSTANCE WmiInstance,
  _In_opt_ ULONG          EventDataSize,
  _In_opt_ PVOID          EventData
);
````


## -parameters
<dl>

### -param <i>WmiInstance</i> [in]

<dd>
<p>A handle to a WMI instance object that the driver obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a>.</p>
</dd>

### -param <i>EventDataSize</i> [in, optional]

<dd>
<p>The size, in bytes, of the event data that <i>EventData</i> points to.</p>
</dd>

### -param <i>EventData</i> [in, optional]

<dd>
<p>A pointer to the event data, or <b>NULL</b> if there is no event data.</p>
</dd>
</dl>

## -returns
<p><b>WdfWmiInstanceFireEvent</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The framework's attempt to communicate with WMI failed.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The event data buffer was too large.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Your driver should call <b>WdfWmiInstanceFireEvent</b> only if a WMI client has registered for event notification. The driver can determine if it should call <b>WdfWmiInstanceFireEvent</b> by providing an <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function or calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>.</p>

<p>The driver should place its event-specific data, if any, in the buffer that the <i>EventData</i> parameter points to. The framework adds all of the necessary WMI header information.</p>

<p>For more information about the <b>WdfWmiInstanceFireEvent</b> method, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example sends a WMI event to WMI clients. </p>

<p>Your driver should call <b>WdfWmiInstanceFireEvent</b> only if a WMI client has registered for event notification. The driver can determine if it should call <b>WdfWmiInstanceFireEvent</b> by providing an <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function or calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>.</p>

<p>The driver should place its event-specific data, if any, in the buffer that the <i>EventData</i> parameter points to. The framework adds all of the necessary WMI header information.</p>

<p>For more information about the <b>WdfWmiInstanceFireEvent</b> method, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example sends a WMI event to WMI clients. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfwmi.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWmiInstanceFireEvent method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
