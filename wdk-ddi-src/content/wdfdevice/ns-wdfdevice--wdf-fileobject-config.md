---
UID: NS.wdfdevice._WDF_FILEOBJECT_CONFIG
title: WDF_FILEOBJECT_CONFIG
author: windows-driver-content
description: The WDF_FILEOBJECT_CONFIG structure contains configuration information of a driver's framework file objects.
old-location: wdf\wdf_fileobject_config.htm
ms.assetid: 6fefc35f-fbbd-4c5e-bb8f-25ad3b6cdb67
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_FILEOBJECT_CONFIG
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
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_FILEOBJECT_CONFIG, WDF_FILEOBJECT_CONFIG, *PWDF_FILEOBJECT_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDF_FILEOBJECT_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_FILEOBJECT_CONFIG</b> structure contains configuration information of a driver's framework file objects. </p>


## -syntax

````
typedef struct _WDF_FILEOBJECT_CONFIG {
  ULONG                      Size;
  PFN_WDF_DEVICE_FILE_CREATE EvtDeviceFileCreate;
  PFN_WDF_FILE_CLOSE         EvtFileClose;
  PFN_WDF_FILE_CLEANUP       EvtFileCleanup;
  WDF_TRI_STATE              AutoForwardCleanupClose;
  WDF_FILEOBJECT_CLASS       FileObjectClass;
} WDF_FILEOBJECT_CONFIG, *PWDF_FILEOBJECT_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>EvtDeviceFileCreate</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtFileClose</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtFileCleanup</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> callback function, or <b>NULL</b>.</p>
</dd>

### -field <b>AutoForwardCleanupClose</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552533">WDF_TRI_STATE</a>-typed value. For more information about this member, see the following Comments section.</p>
</dd>

### -field <b>FileObjectClass</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551315">WDF_FILEOBJECT_CLASS</a>-typed value that identifies whether the driver requires a framework file object to represent each file that an application or another driver creates or opens. Additionally, this value specifies where the framework can store the object's handle. </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_FILEOBJECT_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546107">WdfDeviceInitSetFileObjectConfig</a> method.</p>

<p><b>WDF_FILEOBJECT_CONFIG</b> must be initialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551321">WDF_FILEOBJECT_CONFIG_INIT</a>.</p>

<p>If <b>AutoForwardCleanupClose</b> is set to <b>WdfTrue</b>, the framework does the following:</p>

<p>The framework forwards file creation requests to the next-lower driver if the driver does not provide an <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function and has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff545920">WdfDeviceConfigureRequestDispatching</a> to set an I/O queue to receive file creation requests. The framework does not forward file creation requests if the driver provides a callback function or a queue to handle the requests, so the driver must <a href="wdf.forwarding_i_o_requests">forward</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh406719">complete</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">cancel</a> the requests.</p>

<p>The framework sends file cleanup and close requests to the next-lower driver after calling the driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> and <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback functions.</p>

<p>If <b>AutoForwardCleanupClose</b> is set to <b>WdfFalse</b>, the framework does not forward file creation, cleanup, or close requests. Instead, the framework completes the requests for the driver.</p>

<p>If <b>AutoForwardCleanupClose</b> is set to <b>WdfUseDefault</b>, the framework uses <b>WdfTrue</b> behavior for filter drivers and <b>WdfFalse</b> behavior for function drivers.</p>

<p>Your driver's local I/O target must always receive an equal number of I/O requests with request types of <b>WdfRequestTypeCreate</b>, <b>WdfRequestTypeCleanup</b>, and <b>WdfRequestTypeClose</b>. Therefore, if the driver provides either an <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function or an I/O queue that receives file creation requests, you must use the following rules:</p>

<p>If your driver sets <b>AutoForwardCleanupClose</b> to <b>WdfTrue</b>, the driver must forward all file creation requests to the local I/O target. You must follow this rule because the framework will forward all cleanup and close requests to the local target, whether or not your driver provides <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> and <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback functions.</p>

<p>If your driver sets <b>AutoForwardCleanupClose</b> to <b>WdfFalse</b>, the driver must <i>not</i> forward file creation requests to the local I/O target. You must follow this rule because the framework will <i>not</i> forward cleanup and close requests to the local target, whether or not your driver provides <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> and <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback functions.</p>

<p>If your driver sets <b>AutoForwardCleanupClose</b> to <b>WdfDefault</b>, the driver must follow the rule for <b>WdfTrue</b> if it is a filter driver. The driver must follow the rule for <b>WdfFalse</b> if it is a function driver.</p>

## -requirements
<table>
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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
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