---
UID: NE:wdfrequest._WDF_REQUEST_TYPE
title: "_WDF_REQUEST_TYPE"
author: windows-driver-content
description: The WDF_REQUEST_TYPE enumeration type identifies types of requests that a framework request object might contain.
old-location: wdf\wdf_request_type.htm
old-project: wdf
ms.assetid: 91c036a0-7fce-4c7d-a217-eb1c487a15d0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFRequestObjectRef_43f31fe0-45c1-45d2-adcc-d0d931327eeb.xml, WDF_REQUEST_TYPE, WDF_REQUEST_TYPE enumeration, WdfRequestTypeCleanup, WdfRequestTypeClose, WdfRequestTypeCreate, WdfRequestTypeCreateMailSlot, WdfRequestTypeCreateNamedPipe, WdfRequestTypeDeviceChange, WdfRequestTypeDeviceControl, WdfRequestTypeDeviceControlInternal, WdfRequestTypeDirectoryControl, WdfRequestTypeFileSystemControl, WdfRequestTypeFlushBuffers, WdfRequestTypeLockControl, WdfRequestTypeMax, WdfRequestTypeNoFormat, WdfRequestTypeOther, WdfRequestTypePnp, WdfRequestTypePower, WdfRequestTypeQueryEA, WdfRequestTypeQueryInformation, WdfRequestTypeQueryQuota, WdfRequestTypeQuerySecurity, WdfRequestTypeQueryVolumeInformation, WdfRequestTypeRead, WdfRequestTypeSetEA, WdfRequestTypeSetInformation, WdfRequestTypeSetQuota, WdfRequestTypeSetSecurity, WdfRequestTypeSetVolumeInformation, WdfRequestTypeShutdown, WdfRequestTypeSystemControl, WdfRequestTypeUsb, WdfRequestTypeWrite, _WDF_REQUEST_TYPE, kmdf.wdf_request_type, wdf.wdf_request_type, wdfrequest/WDF_REQUEST_TYPE, wdfrequest/WdfRequestTypeCleanup, wdfrequest/WdfRequestTypeClose, wdfrequest/WdfRequestTypeCreate, wdfrequest/WdfRequestTypeCreateMailSlot, wdfrequest/WdfRequestTypeCreateNamedPipe, wdfrequest/WdfRequestTypeDeviceChange, wdfrequest/WdfRequestTypeDeviceControl, wdfrequest/WdfRequestTypeDeviceControlInternal, wdfrequest/WdfRequestTypeDirectoryControl, wdfrequest/WdfRequestTypeFileSystemControl, wdfrequest/WdfRequestTypeFlushBuffers, wdfrequest/WdfRequestTypeLockControl, wdfrequest/WdfRequestTypeMax, wdfrequest/WdfRequestTypeNoFormat, wdfrequest/WdfRequestTypeOther, wdfrequest/WdfRequestTypePnp, wdfrequest/WdfRequestTypePower, wdfrequest/WdfRequestTypeQueryEA, wdfrequest/WdfRequestTypeQueryInformation, wdfrequest/WdfRequestTypeQueryQuota, wdfrequest/WdfRequestTypeQuerySecurity, wdfrequest/WdfRequestTypeQueryVolumeInformation, wdfrequest/WdfRequestTypeRead, wdfrequest/WdfRequestTypeSetEA, wdfrequest/WdfRequestTypeSetInformation, wdfrequest/WdfRequestTypeSetQuota, wdfrequest/WdfRequestTypeSetSecurity, wdfrequest/WdfRequestTypeSetVolumeInformation, wdfrequest/WdfRequestTypeShutdown, wdfrequest/WdfRequestTypeSystemControl, wdfrequest/WdfRequestTypeUsb, wdfrequest/WdfRequestTypeWrite
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfrequest.h
api_name:
-	WDF_REQUEST_TYPE
product: Windows
targetos: Windows
req.typenames: WDF_REQUEST_TYPE
req.product: Windows 10 or later.
---

# _WDF_REQUEST_TYPE Enumeration
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_REQUEST_TYPE</b> enumeration type identifies types of requests that a framework request object might contain.

## Syntax
```
typedef enum _WDF_REQUEST_TYPE {
  WdfRequestTypeCreate                  ,
  WdfRequestTypeCreateNamedPipe         ,
  WdfRequestTypeClose                   ,
  WdfRequestTypeRead                    ,
  WdfRequestTypeWrite                   ,
  WdfRequestTypeQueryInformation        ,
  WdfRequestTypeSetInformation          ,
  WdfRequestTypeQueryEA                 ,
  WdfRequestTypeSetEA                   ,
  WdfRequestTypeFlushBuffers            ,
  WdfRequestTypeQueryVolumeInformation  ,
  WdfRequestTypeSetVolumeInformation    ,
  WdfRequestTypeDirectoryControl        ,
  WdfRequestTypeFileSystemControl       ,
  WdfRequestTypeDeviceControl           ,
  WdfRequestTypeDeviceControlInternal   ,
  WdfRequestTypeShutdown                ,
  WdfRequestTypeLockControl             ,
  WdfRequestTypeCleanup                 ,
  WdfRequestTypeCreateMailSlot          ,
  WdfRequestTypeQuerySecurity           ,
  WdfRequestTypeSetSecurity             ,
  WdfRequestTypePower                   ,
  WdfRequestTypeSystemControl           ,
  WdfRequestTypeDeviceChange            ,
  WdfRequestTypeQueryQuota              ,
  WdfRequestTypeSetQuota                ,
  WdfRequestTypePnp                     ,
  WdfRequestTypeOther                   ,
  WdfRequestTypeUsb                     ,
  WdfRequestTypeNoFormat                ,
  WdfRequestTypeMax
} WDF_REQUEST_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>WdfRequestTypeCreate</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeCreateNamedPipe</td>
                    <td>The request object represents an <b>IRP_MJ_CREATE_NAMED_PIPE</b> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeClose</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback function.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeRead</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> request. The framework delivers this type of request to a driver's <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/request-handlers">request handler</a>.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeWrite</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> request. The framework delivers this type of request to a driver's <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/request-handlers">request handler</a>.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeQueryInformation</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSetInformation</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeQueryEA</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSetEA</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549346">IRP_MJ_SET_EA</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeFlushBuffers</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeQueryVolumeInformation</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSetVolumeInformation</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeDirectoryControl</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeFileSystemControl</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550751">IRP_MJ_FILE_SYSTEM_CONTROL</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeDeviceControl</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/request-handlers">request handler</a>.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeDeviceControlInternal</td>
                    <td>The request object represents an  <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/request-handlers">request handler</a>.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeShutdown</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="https://msdn.microsoft.com/365e669b-b4a1-432a-ab0c-9292a910256e">EvtDeviceShutdownNotification</a> callback function, if it exists.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeLockControl</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeCleanup</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> callback function.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeCreateMailSlot</td>
                    <td>The request object represents an <b>IRP_MJ_CREATE_MAILSLOT</b> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeQuerySecurity</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSetSecurity</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypePower</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">general</a>, <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">FDO</a>, and <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">PDO</a> callback functions for Plug and Play (PnP) and power management, if the callback functions exist.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSystemControl</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550813">IRP_MJ_SYSTEM_CONTROL</a> request. The framework handles this type of request for the driver, if the driver supports <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/supporting-wmi-in-kmdf-drivers">Windows Management Instrumentation (WMI)</a>.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeDeviceChange</td>
                    <td>The request object represents an <b>IRP_MJ_DEVICE_CHANGE</b> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeQueryQuota</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeSetQuota</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a> request. The framework does not handle this type of request.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypePnp</td>
                    <td>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">general</a>, <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">FDO</a>, and <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn265631">PDO</a> callback functions for PnP and power management, if the callback functions exist.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeOther</td>
                    <td>A driver receives this request type in its <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> event callback function when requests formatted with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548599">WdfIoTargetFormatRequestForInternalIoctlOthers</a> are completed.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeUsb</td>
                    <td>The target device is a USB device. (This value is used only in <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.)</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeNoFormat</td>
                    <td>The request object's type has not been specified.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestTypeMax</td>
                    <td>The maximum value that has been assigned to a valid IRP major function code.</td>
                </tr>
</table>

## Remarks

The <b>WDF_REQUEST_TYPE</b> enumeration type is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552472">WDF_REQUEST_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.

For information about how a framework-based driver can handle request types that the framework does not support, see <a href="https://msdn.microsoft.com/0481f335-f63b-4f93-8eb4-523a70082302">Handling an IRP that the Framework Does Not Support</a>.

For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561467">WDF_REQUEST_TYPE (UMDF)</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfrequest.h (include Wdf.h) |

## See Also

<a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a>



<a href="https://msdn.microsoft.com/365e669b-b4a1-432a-ab0c-9292a910256e">EvtDeviceShutdownNotification</a>



<a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a>



<a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a>