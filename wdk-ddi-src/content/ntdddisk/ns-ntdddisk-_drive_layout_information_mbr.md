---
UID: NS:ntdddisk._DRIVE_LAYOUT_INFORMATION_MBR
title: "_DRIVE_LAYOUT_INFORMATION_MBR"
author: windows-driver-content
description: The DRIVE_LAYOUT_INFORMATION_MBR structure reports the drive signature for a Master Boot Record partition.
old-location: storage\drive_layout_information_mbr.htm
old-project: storage
ms.assetid: 41df2847-7cfa-4746-82bd-d0b8b482a0d4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDRIVE_LAYOUT_INFORMATION_MBR, DRIVE_LAYOUT_INFORMATION_MBR, DRIVE_LAYOUT_INFORMATION_MBR structure [Storage Devices], PDRIVE_LAYOUT_INFORMATION_MBR, PDRIVE_LAYOUT_INFORMATION_MBR structure pointer [Storage Devices], _DRIVE_LAYOUT_INFORMATION_MBR, ntdddisk/DRIVE_LAYOUT_INFORMATION_MBR, ntdddisk/PDRIVE_LAYOUT_INFORMATION_MBR, storage.drive_layout_information_mbr, structs-disk_766d8fbf-64c1-4b4e-b0ce-421c8892b0d4.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntddk.h
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
-	ntdddisk.h
api_name:
-	DRIVE_LAYOUT_INFORMATION_MBR
product:
- Windows
targetos: Windows
req.typenames: DRIVE_LAYOUT_INFORMATION_MBR, *PDRIVE_LAYOUT_INFORMATION_MBR
---

# _DRIVE_LAYOUT_INFORMATION_MBR structure


## -description


The DRIVE_LAYOUT_INFORMATION_MBR structure reports the drive signature for a Master Boot Record partition. 


## -struct-fields




### -field Signature

Specifies the disk signature value, which uniquely identifies the disk. 


### -field CheckSum

 




## -remarks



This structure contains the drive layout information that is specific to a drive with a Master Boot Record partition. It is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a> structure.




## -see-also




<a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561452">IoReadPartitionTable</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>
 

 

