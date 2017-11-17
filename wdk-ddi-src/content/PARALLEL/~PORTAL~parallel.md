# Declarations in the parallel header
This header Parallel contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PARALLEL_INTERRUPT_SERVICE_ROUTINE structure](ns-parallel--parallel-interrupt-service-routine.md) | The PARALLEL_INTERRUPT_SERVICE_ROUTINE structure specifies interrupt services that a kernel-mode driver can connect to the operation of a parallel port. |
| [PARPORT_REMOVAL_RELATIONS structure](ns-parallel--parport-removal-relations.md) | TBD |
| [PARALLEL_PORT_INFORMATION structure](ns-parallel--parallel-port-information.md) | The PARALLEL_PORT_INFORMATION structure specifies information about the resources assigned to a parallel port, the capabilities of the parallel port, and pointers to callback routines that a kernel-mode driver can use to operate the parallel port. |
| [PARALLEL_PARCHIP_INFO structure](ns-parallel--parallel-parchip-info.md) | TBD |
| [PARALLEL_1284_COMMAND structure](ns-parallel--parallel-1284-command.md) | The PARALLEL_1284_COMMAND structure specifies information that a client uses to select and deselect an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device. |
| [MORE_PARALLEL_PORT_INFORMATION structure](ns-parallel--more-parallel-port-information.md) | The MORE_PARALLEL_PORT_INFORMATION structure specifies information about the system interface that supports the operation of a parallel port. |
| [PARALLEL_CHIP_MODE structure](ns-parallel--parallel-chip-mode.md) | The PARALLEL_CHIP_MODE structure specifies the operating mode of a parallel port. |
| [PARALLEL_INTERRUPT_INFORMATION structure](ns-parallel--parallel-interrupt-information.md) | The PARALLEL_INTERRUPT_INFORMATION structure specifies information that a kernel-mode driver can use in the context of an ISR that the driver connects to a parallel port. |
| [PARALLEL_PNP_INFORMATION structure](ns-parallel--parallel-pnp-information.md) | The PARALLEL_PNP_INFORMATION structure specifies information about the capabilities of a parallel port. |
| [PARCLASS_INFORMATION structure](ns-parallel--parclass-information.md) | The PARCLASS_INFORMATION structure specifies information about a parallel port, pointers to callback routines to operate a parallel port, and pointers to callback routines to read and write to a parallel device. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_PARALLEL_PORT_FREE IOCTL](ni-parallel-ioctl-internal-parallel-port-free.md) | The IOCTL_INTERNAL_PARALLEL_PORT_FREE request frees a parallel port. |
| [IOCTL_INTERNAL_PARCLASS_CONNECT IOCTL](ni-parallel-ioctl-internal-parclass-connect.md) | The IOCTL_INTERNAL_PARCLASS_CONNECT request returns information about a parallel port and the callback routines that the system-supplied bus driver for parallel ports provides to operate the parallel port. |
| [IOCTL_INTERNAL_DESELECT_DEVICE IOCTL](ni-parallel-ioctl-internal-deselect-device.md) | The IOCTL_INTERNAL_DESELECT_DEVICE request deselects an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device attached to a parallel port. |
| [IOCTL_INTERNAL_ENABLE_END_OF_CHAIN_BUS_RESCAN IOCTL](ni-parallel-ioctl-internal-enable-end-of-chain-bus-rescan.md) | TBD |
| [IOCTL_INTERNAL_PARCLASS_DISCONNECT IOCTL](ni-parallel-ioctl-internal-parclass-disconnect.md) | The IOCTL_INTERNAL_PARCLASS_DISCONNECT request disconnects a client from a parallel device. |
| [IOCTL_INTERNAL_LOCK_PORT_NO_SELECT IOCTL](ni-parallel-ioctl-internal-lock-port-no-select.md) | The IOCTL_INTERNAL_LOCK_PORT_NO_SELECT request allocates the parallel device's parent parallel port, but does not select the parallel device. |
| [IOCTL_INTERNAL_PARDOT3_RESET IOCTL](ni-parallel-ioctl-internal-pardot3-reset.md) | TBD |
| [IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO IOCTL](ni-parallel-ioctl-internal-get-parallel-port-info.md) | The IOCTL_INTERNAL_GET_PARALLEL_PORT_INFO request returns information about a parallel port. |
| [IOCTL_INTERNAL_DISABLE_END_OF_CHAIN_BUS_RESCAN IOCTL](ni-parallel-ioctl-internal-disable-end-of-chain-bus-rescan.md) | TBD |
| [IOCTL_INTERNAL_UNLOCK_PORT IOCTL](ni-parallel-ioctl-internal-unlock-port.md) | The IOCTL_INTERNAL_UNLOCK_PORT request deselects a parallel device and frees the parallel device's parent parallel port. |
| [IOCTL_INTERNAL_REGISTER_FOR_REMOVAL_RELATIONS IOCTL](ni-parallel-ioctl-internal-register-for-removal-relations.md) | TBD |
| [IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE IOCTL](ni-parallel-ioctl-internal-parallel-set-chip-mode.md) | The IOCTL_INTERNAL_PARALLEL_SET_CHIP_MODE request sets the operating mode of a parallel port. |
| [IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT IOCTL](ni-parallel-ioctl-internal-parallel-connect-interrupt.md) | The IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT request connects an optional interrupt service routine and an optional deferred port check routine to a parallel port. |
| [IOCTL_INTERNAL_PARDOT3_DISCONNECT IOCTL](ni-parallel-ioctl-internal-pardot3-disconnect.md) | TBD |
| [IOCTL_INTERNAL_PARDOT3_CONNECT IOCTL](ni-parallel-ioctl-internal-pardot3-connect.md) | TBD |
| [IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO IOCTL](ni-parallel-ioctl-internal-get-more-parallel-port-info.md) | The IOCTL_INTERNAL_GET_MORE_PARALLEL_PORT_INFO request returns information about a parallel port. |
| [IOCTL_INTERNAL_PARDOT3_SIGNAL IOCTL](ni-parallel-ioctl-internal-pardot3-signal.md) | TBD |
| [IOCTL_INTERNAL_GET_PARPORT_FDO IOCTL](ni-parallel-ioctl-internal-get-parport-fdo.md) | TBD |
| [IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT IOCTL](ni-parallel-ioctl-internal-parallel-disconnect-interrupt.md) | The IOCTL_INTERNAL_PARALLEL_DISCONNECT_INTERRUPT request disconnects an interrupt service routine (and an optional deferred port check service routine) that was connected by using an IOCTL_INTERNAL_PARALLEL_CONNECT_INTERRUPT request. |
| [IOCTL_INTERNAL_UNLOCK_PORT_NO_DESELECT IOCTL](ni-parallel-ioctl-internal-unlock-port-no-deselect.md) | The IOCTL_INTERNAL_UNLOCK_PORT_NO_DESELECT request frees a parallel device's parent parallel port. |
| [IOCTL_INTERNAL_SELECT_DEVICE IOCTL](ni-parallel-ioctl-internal-select-device.md) | The IOCTL_INTERNAL_SELECT_DEVICE request |
| [IOCTL_INTERNAL_PARALLEL_PORT_ALLOCATE IOCTL](ni-parallel-ioctl-internal-parallel-port-allocate.md) | The IOCTL_INTERNAL_PARALLEL_PORT_ALLOCATE request allocates a parallel port for exclusive access by a client. |
| [IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO IOCTL](ni-parallel-ioctl-internal-get-parallel-pnp-info.md) | The IOCTL_INTERNAL_GET_PARALLEL_PNP_INFO request returns Plug and Play information about a parallel port. |
| [IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE IOCTL](ni-parallel-ioctl-internal-parallel-clear-chip-mode.md) | The IOCTL_INTERNAL_PARALLEL_CLEAR_CHIP_MODE request clears the operating mode of a parallel port. |
| [IOCTL_INTERNAL_PARCHIP_CONNECT IOCTL](ni-parallel-ioctl-internal-parchip-connect.md) | TBD |
| [IOCTL_INTERNAL_UNREGISTER_FOR_REMOVAL_RELATIONS IOCTL](ni-parallel-ioctl-internal-unregister-for-removal-relations.md) | TBD |
| [IOCTL_INTERNAL_RELEASE_PARALLEL_PORT_INFO IOCTL](ni-parallel-ioctl-internal-release-parallel-port-info.md) | The IOCTL_INTERNAL_RELEASE_PARALLEL_PORT_INFO request returns STATUS_SUCCESS. |
| [IOCTL_INTERNAL_INIT_1284_3_BUS IOCTL](ni-parallel-ioctl-internal-init-1284-3-bus.md) | The IOCTL_INTERNAL_INIT_1284_3_BUS request initializes and assigns an IEEE 1284.3 device ID to all the 1284.3 daisy chain devices that are attached to a parallel port. |
| [IOCTL_INTERNAL_LOCK_PORT IOCTL](ni-parallel-ioctl-internal-lock-port.md) | The IOCTL_INTERNAL_LOCK_PORT request allocates the parallel device's parent parallel port and selects the parallel device on the port. |
| [IOCTL_INTERNAL_DISCONNECT_IDLE IOCTL](ni-parallel-ioctl-internal-disconnect-idle.md) | The IOCTL_INTERNAL_DISCONNECT_IDLE request disconnects the IEEE 1284 operating modes that are set for a parallel device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PARALLEL_SAFETY enumeration](ne-parallel-parallel-safety.md) | TBD |
| [P1284_HW_MODE enumeration](ne-parallel-p1284-hw-mode.md) | TBD |
| [P12843_DL_MODES enumeration](ne-parallel-p12843-dl-modes.md) | TBD |
| [P1284_PHASE enumeration](ne-parallel-p1284-phase.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PPARALLEL_TRY_ALLOCATE_ROUTINE callback](nc-parallel-pparallel-try-allocate-routine.md) | The PPARALLEL_TRY_ALLOCATE_ROUTINE-typed callback routine is a nonblocking routine that attempts to allocate a parallel port. The system-supplied function driver for parallel ports supplies this routine. |
| [PDETERMINE_IEEE_MODES callback](nc-parallel-pdetermine-ieee-modes.md) | The PDETERMINE_IEEE_MODES-typed callback routine determines which IEEE 1284 protocols a parallel device supports. The system-supplied bus driver for parallel ports supplies this routine. |
| [PNEGOTIATE_IEEE_MODE callback](nc-parallel-pnegotiate-ieee-mode~r1.md) | The PNEGOTIATE_IEEE_MODE-typed callback routine selects the fastest forward and reverse protocols that the system-supplied bus driver for parallel ports supports from among those specified by the caller. |
| [PPARCHIP_CLEAR_CHIP_MODE callback function](nc-parallel-pparchip-clear-chip-mode.md) | TBD |
| [PPARALLEL_DESELECT_ROUTINE callback](nc-parallel-pparallel-deselect-routine.md) | The PPARALLEL_DESELECT_ROUTINE-typed callback routine deselects either an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port. |
| [PPARALLEL_IEEE_FWD_TO_REV callback](nc-parallel-pparallel-ieee-fwd-to-rev.md) | The PPARALLEL_IEEE_FWD_TO_REV-typed callback routine changes the transfer mode from forward to reverse. The system-supplied bus driver for parallel ports supplies this routine. |
| [PPARALLEL_IEEE_REV_TO_FWD callback](nc-parallel-pparallel-ieee-rev-to-fwd.md) | The PPARALLEL_IEEE_REV_TO_FWD-typed callback routine changes the transfer mode from reverse to forward. The system-supplied bus driver for parallel ports supplies this routine. |
| [PPARALLEL_CLEAR_CHIP_MODE callback](nc-parallel-pparallel-clear-chip-mode.md) | The PPARALLEL_CLEAR_CHIP_MODE-typed callback routine clears the operating mode of a parallel port by resetting the communication mode of the host chipset to IEEE 1284-compatibility mode. |
| [PPARALLEL_SET_CHIP_MODE callback](nc-parallel-pparallel-set-chip-mode.md) | The PPARALLEL_SET_CHIP_MODE-typed callback routine sets the operating mode of a parallel port. The system-supplied function driver for parallel ports supplies this routine. |
| [PPARCHIP_SET_CHIP_MODE callback function](nc-parallel-pparchip-set-chip-mode.md) | TBD |
| [PPARALLEL_DEFERRED_ROUTINE callback function](nc-parallel-pparallel-deferred-routine.md) | TBD |
| [PPARALLEL_FREE_ROUTINE callback](nc-parallel-pparallel-free-routine.md) | The PPARALLEL_FREE_ROUTINE-typed callback routine frees a parallel port. The system-supplied function driver for parallel ports supplies this routine. |
| [PPARALLEL_DESELECT_DEVICE callback function](nc-parallel-pparallel-deselect-device.md) | TBD |
| [PPARALLEL_TRYSELECT_DEVICE callback function](nc-parallel-pparallel-tryselect-device.md) | TBD |
| [PPARALLEL_TRY_SELECT_ROUTINE callback](nc-parallel-pparallel-try-select-routine.md) | The PPARALLEL_TRY_SELECT_ROUTINE-typed callback routine selects an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port. The system-supplied function driver for parallel ports supplies this routine. |
| [PPARALLEL_QUERY_WAITERS_ROUTINE callback](nc-parallel-pparallel-query-waiters-routine.md) | The PPARALLEL_QUERY_WAITERS_ROUTINE-typed callback routine returns the number of IOCTL_INTERNAL_PARALLEL_PORT_ALLOCATE and IOCTL_INTERNAL_SELECT_DEVICE requests that are queued on the work queue of a parallel port. |
| [PTERMINATE_IEEE_MODE callback](nc-parallel-pterminate-ieee-mode.md) | The PTERMINATE_IEEE_MODE-typed callback routine terminates the current IEEE operating mode and sets the mode to IEEE 1284-compatible. The system-supplied bus driver for parallel ports supplies this routine. |
| [PNEGOTIATE_IEEE_MODE callback](nc-parallel-pnegotiate-ieee-mode.md) | The PNEGOTIATE_IEEE_MODE-typed callback routine selects the fastest forward and reverse protocols that the system-supplied bus driver for parallel ports supports from among those specified by the caller. |
| [PPARALLEL_WRITE callback](nc-parallel-pparallel-write.md) | The PPARALLEL_WRITE-typed callback routine writes data to a parallel device. The system-supplied bus driver for parallel ports supplies this routine. |
| [PPARALLEL_READ callback](nc-parallel-pparallel-read.md) | The PPARALLEL_READ-typed callback routine reads data from a parallel device. The system-supplied bus driver for parallel ports supplies this routine. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [TEST_ECR_FIFO function](nf-parallel-test-ecr-fifo.md) | TBD |
| [SET_DCR function](nf-parallel-set-dcr.md) | TBD |

This header is used in these topics:

- [parports](..content/_parports)
