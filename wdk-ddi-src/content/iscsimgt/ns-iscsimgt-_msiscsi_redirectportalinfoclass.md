---
UID : NS:iscsimgt._MSiSCSI_RedirectPortalInfoClass
title : _MSiSCSI_RedirectPortalInfoClass
author : windows-driver-content
description : The MSiSCSI_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.
old-location : storage\msiscsi_redirectportalinfoclass.htm
old-project : storage
ms.assetid : fcddf029-748b-4300-9f87-a103d961918a
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _MSiSCSI_RedirectPortalInfoClass, MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iscsimgt.h
req.include-header : Iscsimgt.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : MSiSCSI_RedirectPortalInfoClass
req.alt-loc : iscsimgt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass
---

# _MSiSCSI_RedirectPortalInfoClass structure
The MSiSCSI_RedirectPortalInfoClass structure contains information about a collection of sessions for an adapter ID. It also contains the portal redirection information for each of the sessions.

## Syntax
````
typedef struct _MSiSCSI_RedirectPortalInfoClass {
  ULONGLONG                 UniqueAdapterId;
  ULONG                     SessionCount;
  ISCSI_RedirectSessionInfo RedirectSessionList[1];
} MSiSCSI_RedirectPortalInfoClass, *PMSiSCSI_RedirectPortalInfoClass;
````

## Members

        
            `RedirectSessionList`

            An array of structures that contains as many ISCSI_RedirectSessionInfo structures as specified in the connection count.
        
            `SessionCount`

            The number of sessions for which this structure contains information.
        
            `UniqueAdapterId`

            A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this identifier (ID).

    ## Remarks
        You must implement this class if the adapter supports target portal hopping. Otherwise, it is optional.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iscsimgt.h (include Iscsimgt.h) |