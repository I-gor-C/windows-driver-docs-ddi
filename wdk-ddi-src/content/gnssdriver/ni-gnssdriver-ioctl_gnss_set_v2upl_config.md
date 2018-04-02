---
UID: NI:gnssdriver.IOCTL_GNSS_SET_V2UPL_CONFIG
title: IOCTL_GNSS_SET_V2UPL_CONFIG
author: windows-driver-content
description: The IOCTL_GNSS_SET_V2UPL_CONFIG control code is used by the GNSS adapter to set configuration for v2 user plane location for CDMA, which consist of the MPC address, and in testing mode, potentially the PDE address.
old-location: sensors\ioctl_gnss_set_v2upl_config.htm
old-project: sensors
ms.assetid: 7E06DAAF-B360-4C6C-8E6B-0F7CFC46A69E
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: IOCTL_GNSS_SET_V2UPL_CONFIG, IOCTL_GNSS_SET_V2UPL_CONFIG control code [Sensor Devices], gnssdriver/IOCTL_GNSS_SET_V2UPL_CONFIG, sensors.ioctl_gnss_set_v2upl_config
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
-	gnssdriver.h
api_name:
-	IOCTL_GNSS_SET_V2UPL_CONFIG
product: Windows
targetos: Windows
req.typenames: GNSS_SUPL_CERT_ACTION
---

# IOCTL_GNSS_SET_V2UPL_CONFIG IOCTL
The <b>IOCTL_GNSS_SET_V2UPL_CONFIG</b> control code is used by the GNSS adapter to set configuration for v2 user plane location for CDMA, which consist of the MPC address, and in testing mode, potentially the PDE address.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925235">GNSS_V2UPL_CONFIG</a> structure.

### Input Buffer Length
Set to sizeof(GNSS_V2UPL_CONFIG).

### Output Buffer
Set to NULL.

### Output Buffer Length
Set to 0.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
<b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code.

## Remarks
The driver sets one of the following NTSTATUS values to indicate the result.

<ul>
<li>
<b>STATUS_SUCCESS</b>, when the driver processes the V2UPL information successfully.

</li>
<li>
<b>Failed</b>, when the driver does not process the V2UPL information successfully.

</li>
<li>
<b>Ignored</b>, when the driver ignores the V2UPL information.

</li>
</ul>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | gnssdriver.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>