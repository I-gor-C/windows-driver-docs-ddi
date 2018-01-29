---
UID : NF:storport.StorPortSetPowerSettingNotificationGuids
title : StorPortSetPowerSettingNotificationGuids function
author : windows-driver-content
description : The StorPortSetPowerSettingNotificationGuids routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for.
old-location : storage\storportsetpowersettingnotificationguids.htm
old-project : storage
ms.assetid : FB74E774-8CDE-4DE4-942E-10AF4BEFF63C
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : StorPortSetPowerSettingNotificationGuids routine [Storage Devices], StorPortSetPowerSettingNotificationGuids, Adaptive Setting, storage.storportsetpowersettingnotificationguids, storport/StorPortSetPowerSettingNotificationGuids, HIPM/DIPM Setting
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : storport.h
req.include-header : Storport.h
req.target-type : Universal
req.target-min-winverclnt : Available in starting with Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : Any
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : STOR_SPINLOCK
req.product : Windows 10 or later.
---


# StorPortSetPowerSettingNotificationGuids function
The <b>StorPortSetPowerSettingNotificationGuids</b> routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for.

## Syntax

````
ULONG StorPortSetPowerSettingNotificationGuids(
  _In_ PVOID  HwDeviceExtension,
  _In_ ULONG  GuidCount,
  _In_ LPGUID Guid
);
````

## Parameters

`HwDeviceExtension`

A pointer to the hardware device extension for the host bus adapter (HBA).

`GuidCount`

The number of GUIDs in the <i>Guid</i> array.

`Guid`

An array of power setting GUIDs to register for notification. A typical use for registering these GUIDs is for SATA miniports to receive notifications for AHCI Link Power Management setting changes. The  AHCI Link Power Management settings defined by the Microsoft AHCI StorPort miniport driver are the following.

Other miniports may define and register their own power setting GUIDs.


## Return Value

The <b>StorPortSetPowerSettingNotificationGuids</b> routine returns one of these status codes:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
 Insufficient resources are available to register for notifications.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The notification GUIDs were registered successfully.

</td>
</tr>
</table>

## Remarks

A miniport calls <b>StorPortSetPowerSettingNotificationGuids</b> in its <a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a> routine to register the GUIDs it requests to receive notifications for.

When a power state change occurs for a registered notification, the miniport is notified in its <a href="..\storport\nc-storport-hw_adapter_control.md">HwStorAdapterControl</a> routine. The control type of <b>ScsiPowerSettingNotification</b> is set in the <i>ControlType</i> parameter.

The AHCI Link Power management settings are part of the Disk Settings subgroup (0012ee47-9041-4b5d-9b77-535fba8b1442) in the power policy configuration. These are managed under the SUB_DISK configuration  alias with <i>powercfg.exe</i>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h (include Storport.h) |
| **Library** |  |
| **IRQL** | Any |
| **DDI compliance rules** |  |

## See Also

<a href="..\storport\nc-storport-hw_adapter_control.md">HwStorAdapterControl</a>

<a href="..\storport\nc-storport-hw_find_adapter.md">HwStorFindAdapter</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortSetPowerSettingNotificationGuids routine%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>