# the class is named after the base model of the vehicle, with the T-55 being a MBT (Main Battle Tank)
class T55:

    # the vehicle has several attributes, like its model (ex: a, b, b3), main gun, coax, aa gun and health
    # these specifications are individual of each vehicle
    def __init__(self, model, gun, reload_time, coax, aa_gun, hitpoints):
        self.model = model
        self.gun = gun
        self.reload_time = reload_time
        self.coax = coax
        self.aa_gun = aa_gun
        self.hitpoints = hitpoints

    # this is a little function created to increment the specs menu. It's separated from the specs method to allow it's repositioning
    def tank_history(self):
        print("Introduced in the following years after WW2, this all-around MBT was the backbone of the Warsaw Pact armored columns, with a powerful 100mm rifled gun and good angled armor.")

    # these functions are the main commands of which the player will make use throughout the gameplay
    def fire_main_gun(self):
        print("On the way! (the gunner fires the main gun)")

    def reloading(self):
        print("(reloading...")

    def fire_coax(self):
        print("TAKATAKATAKATAKATAKATAKATAKATAKATAKA... (the gunner fires the coax)")

    def fire_aa_gun(self):
        print("BUMBUMBUMBUMBUM... (the commander fires the AA gun)")

    def move_forward(self):
        print("Driver, crank it! (the vehicle steers forward)")

    def move_backward(self):
        print("Driver, fall back! (the vehicle steers backward)")

    # this function will be called whenever the player achieves the research progress
    def upgrade(self):
        self.model = "T-55A"
        self.gun = "D-10T2S 100mm rifled gun"
        self.reload_time = 10
        self.coax = "SGMT 7.62mm light machine gun"
        self.aa_gun = "DShK 12.7mm heavy machine gun"
        self.hitpoints = 15500

        print("Your vehicle was retrofited with newly developed parts!")

    # this function will be used to pop the current vehicle's specifications on the hangar
    def specs(self):
        output = f"""
        Model: {t55.model}
        Gun: {t55.gun}
        Reload time: {t55.reload_time}/s
        Coax: {t55.coax}
        AA Gun: {t55.aa_gun}
        Hitpoints: {t55.hitpoints}
        """

        print(output)


if __name__ == '__main__':

    t55 = T55("T-55", "D-10T 100mm rifled gun", 15, "SGMT 7.62mm light machine gun", "No AA Gun", 1450)

    t55.tank_history()
    t55.specs()

    print("Press '1' to Upgrade or '2' to exit. \n")
    choice = int(input("Choose: "))

    if choice == 1:
        t55.upgrade()
        t55.specs()

    elif choice == 2:
        print("Returning to the menu...")

    else:
        while 1 or 2 not in choice:
            print("Wrong choice! Press '1' to Upgrade or '2' to exit!\n")
            choice2 = int(input("Choose: "))

            if choice2 == 1:
                t55.upgrade()
                t55.specs()
                break

            elif choice2 == 2:
                print("Returning to the menu...")

            else:
                continue
