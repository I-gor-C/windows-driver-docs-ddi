---
UID: NE:minitape.PSTOR_POWER_ACTION
title: "*PSTOR_POWER_ACTION"
author: windows-driver-content
description: The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition.
old-location: storage\stor_power_action.htm
old-project: storage
ms.assetid: ffc7c1ec-faec-4383-ab69-844cf68d054f
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PSTOR_POWER_ACTION, PSTOR_POWER_ACTION, PSTOR_POWER_ACTION enumeration pointer [Storage Devices], STOR_POWER_ACTION, STOR_POWER_ACTION enumeration [Storage Devices], StorPowerActionHibernate, StorPowerActionNone, StorPowerActionReserved, StorPowerActionShutdown, StorPowerActionShutdownOff, StorPowerActionShutdownReset, StorPowerActionSleep, StorPowerActionWarmEject, storage.stor_power_action, storport/PSTOR_POWER_ACTION, storport/STOR_POWER_ACTION, storport/StorPowerActionHibernate, storport/StorPowerActionNone, storport/StorPowerActionReserved, storport/StorPowerActionShutdown, storport/StorPowerActionShutdownOff, storport/StorPowerActionShutdownReset, storport/StorPowerActionSleep, storport/StorPowerActionWarmEject, structs-storport_53754a67-bd34-4f06-92ba-2f45d7fa66a9.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: minitape.h
req.include-header: Storport.h, Minitape.h, Srb.h
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
-	storport.h
api_name:
-	STOR_POWER_ACTION
product:
- Windows
targetos: Windows
req.typenames: STOR_POWER_ACTION, *PSTOR_POWER_ACTION
---

# *PSTOR_POWER_ACTION Enumeration
The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition.

## Syntax
````
typedef enum  { 
  StorPowerActionNone           = 0,
  StorPowerActionReserved       = 1,
  StorPowerActionSleep          = 2,
  StorPowerActionHibernate      = 3,
  StorPowerActionShutdown       = 4,
  StorPowerActionShutdownReset  = 5,
  StorPowerActionShutdownOff    = 6,
  StorPowerActionWarmEject      = 7
} STOR_POWER_ACTION, *PSTOR_POWER_ACTION;
````

## Constants

<table>
            
                <tr>
                    <td>StorPowerActionNone</td>
                    <td>No system shutdown is about to occur.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionReserved</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionSleep</td>
                    <td>The system is entering standby.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionHibernate</td>
                    <td>The system is entering hibernation.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdown</td>
                    <td>The system is shutting down, but the type of shutdown is not known.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdownReset</td>
                    <td>The system is shutting down and resetting.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdownOff</td>
                    <td>The system is shutting down and powering off.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionWarmEject</td>
                    <td>The system is preparing for ejection.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | minitape.h (include Storport.h, Minitape.h, Srb.h) |

## See Also

<a href="..\storport\ns-storport-_scsi_power_request_block.md">SCSI_POWER_REQUEST_BLOCK</a>