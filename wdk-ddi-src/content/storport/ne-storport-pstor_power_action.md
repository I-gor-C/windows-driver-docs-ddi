---
UID: NE:storport.PSTOR_POWER_ACTION
title: "*PSTOR_POWER_ACTION"
author: windows-driver-content
description: The STOR_POWER_ACTION enumerator indicates the power state that the system is about to enter during a power transition.
old-location: storage\stor_power_action.htm
old-project: storage
ms.assetid: ffc7c1ec-faec-4383-ab69-844cf68d054f
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: "*PSTOR_POWER_ACTION, storport/StorPowerActionShutdownReset, STOR_POWER_ACTION enumeration [Storage Devices], PSTOR_POWER_ACTION enumeration pointer [Storage Devices], StorPowerActionHibernate, storport/StorPowerActionSleep, StorPowerActionShutdown, StorPowerActionSleep, StorPowerActionNone, StorPowerActionWarmEject, PSTOR_POWER_ACTION, StorPowerActionShutdownReset, storport/StorPowerActionShutdownOff, storport/StorPowerActionReserved, storage.stor_power_action, storport/PSTOR_POWER_ACTION, storport/StorPowerActionHibernate, storport/StorPowerActionShutdown, StorPowerActionReserved, storport/STOR_POWER_ACTION, storport/StorPowerActionWarmEject, StorPowerActionShutdownOff, STOR_POWER_ACTION, storport/StorPowerActionNone, structs-storport_53754a67-bd34-4f06-92ba-2f45d7fa66a9.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: storport.h
req.include-header: Storport.h
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	storport.h
apiname:
-	STOR_POWER_ACTION
product: Windows
targetos: Windows
req.typenames: STOR_POWER_ACTION, *PSTOR_POWER_ACTION
req.product: Windows 10 or later.
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
                    <td>StorPowerActionHibernate</td>
                    <td>The system is entering hibernation.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionNone</td>
                    <td>No system shutdown is about to occur.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionReserved</td>
                    <td>Reserved.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdown</td>
                    <td>The system is shutting down, but the type of shutdown is not known.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdownOff</td>
                    <td>The system is shutting down and powering off.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionShutdownReset</td>
                    <td>The system is shutting down and resetting.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionSleep</td>
                    <td>The system is entering standby.</td>
                </tr>
            
                <tr>
                    <td>StorPowerActionWarmEject</td>
                    <td>The system is preparing for ejection.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | storport.h (include Storport.h) |

    ## See Also

        <a href="..\storport\ns-storport-_scsi_power_request_block.md">SCSI_POWER_REQUEST_BLOCK</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STOR_POWER_ACTION enumeration%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>