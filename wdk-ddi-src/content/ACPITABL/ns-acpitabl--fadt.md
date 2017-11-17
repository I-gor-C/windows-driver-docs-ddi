---
UID: NS.acpitabl._FADT
title: FADT
author: windows-driver-content
description: 
ms.assetid: 9e1eb87a-2c4e-4f0d-9e2a-b50a2430d1be
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: FADT, FADT, *PFADT
req.header: acpitabl.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# FADT structure

## -description



## -struct-fields

### -field DESCRIPTION_HEADER Header			
 	
### -field ULONG facs			
 	
### -field ULONG dsdt			
 	
### -field UCHAR int_model			
 	
### -field UCHAR pm_profile			
 	
### -field USHORT sci_int_vector			
 	
### -field ULONG smi_cmd_io_port			
 	
### -field UCHAR acpi_on_value			
 	
### -field UCHAR acpi_off_value			
 	
### -field UCHAR s4bios_req			
 	
### -field UCHAR pstate_control			
 	
### -field ULONG pm1a_evt_blk_io_port			
 	
### -field ULONG pm1b_evt_blk_io_port			
 	
### -field ULONG pm1a_ctrl_blk_io_port			
 	
### -field ULONG pm1b_ctrl_blk_io_port			
 	
### -field ULONG pm2_ctrl_blk_io_port			
 	
### -field ULONG pm_tmr_blk_io_port			
 	
### -field ULONG gp0_blk_io_port			
 	
### -field ULONG gp1_blk_io_port			
 	
### -field UCHAR pm1_evt_len			
 	
### -field UCHAR pm1_ctrl_len			
 	
### -field UCHAR pm2_ctrl_len			
 	
### -field UCHAR pm_tmr_len			
 	
### -field UCHAR gp0_blk_len			
 	
### -field UCHAR gp1_blk_len			
 	
### -field UCHAR gp1_base			
 	
### -field UCHAR cstate_control			
 	
### -field USHORT lvl2_latency			
 	
### -field USHORT lvl3_latency			
 	
### -field USHORT flush_size			
 	
### -field USHORT flush_stride			
 	
### -field UCHAR duty_offset			
 	
### -field UCHAR duty_width			
 	
### -field UCHAR day_alarm_index			
 	
### -field UCHAR month_alarm_index			
 	
### -field UCHAR century_alarm_index			
 	
### -field USHORT boot_arch			
 	
### -field UCHAR [1] reserved3			
 	
### -field ULONG flags			
 	
### -field GEN_ADDR reset_reg			
 	
### -field UCHAR reset_val			
 	
### -field USHORT arm_boot_arch			
 	
### -field UCHAR minor_version_number			
 	
### -field PHYSICAL_ADDRESS x_firmware_ctrl			
 	
### -field PHYSICAL_ADDRESS x_dsdt			
 	
### -field GEN_ADDR x_pm1a_evt_blk			
 	
### -field GEN_ADDR x_pm1b_evt_blk			
 	
### -field GEN_ADDR x_pm1a_ctrl_blk			
 	
### -field GEN_ADDR x_pm1b_ctrl_blk			
 	
### -field GEN_ADDR x_pm2_ctrl_blk			
 	
### -field GEN_ADDR x_pm_tmr_blk			
 	
### -field GEN_ADDR x_gp0_blk			
 	
### -field GEN_ADDR x_gp1_blk			
 	
### -field GEN_ADDR sleep_control_reg			
 	
### -field GEN_ADDR sleep_status_reg			
 	
## -remarks

## -see-also